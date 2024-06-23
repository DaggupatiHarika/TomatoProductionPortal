# market/views.py
from django.shortcuts import render
from django.views.generic import ListView
from .models import Market, State, District, Price

def market_map(request):
    markets = Market.objects.all()
    return render(request, 'market/market_map.html', {'markets': markets})

def market_graph(request, **kwargs):
    market = Market.objects.get(id = kwargs['pk'])
    price_list = Price.objects.filter(market=market).order_by('date')[:30]
    context={'market':market, 'price_list':price_list}
    return render(request, 'market/market_graph.html', context)


class MarketListView(ListView):
    model = Market
    template_name = 'market/market_list.html'
    context_object_name = 'markets'

    def get_queryset(self):
        queryset = super().get_queryset()
        state_id = self.request.GET.get('state', None)
        district_id = self.request.GET.get('district', None)

        if state_id:
            queryset = queryset.filter(state_id=state_id)
        if district_id:
            queryset = queryset.filter(district_id=district_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['states'] = State.objects.all()
        return context

