import time
from datetime import datetime
from django.db.models import Avg, Sum,Count
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
import json
from django.urls import path
from django.core.cache import cache
from django.contrib import messages
from .models import my_table
import locale
from json import dumps
locale.setlocale(locale.LC_ALL, 'en_IN')
from django.http import JsonResponse
from django.shortcuts import redirect

values = {}
class PowerBIDashboardView(TemplateView):
    template_name = 'sales_dashboard_using_powerBI.html'



class python_dashput(TemplateView):
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated==True:
            global values
            
            print(values)
            if 'Month' in values:
                month = values['Month']
                month = ["'".join(i.split("-")) for i in month]
                values['Month'] = month
            print(values)   
            pretime = datetime.now()
            pretime1 = pretime
            queryset = my_table.objects.using('mysql_db').all()
            paid_status = queryset.values_list('paid_status', flat=True).distinct()
            paid_status = [paid_status for paid_status in paid_status]
            zone = queryset.values_list('zone', flat=True).distinct()
            zone = [zone for zone in zone]
            month = queryset.values_list('month', flat=True).distinct()
            month = ["-".join(month.split("'")) for month in month]
            loan_type = queryset.values_list('product', flat=True).distinct()
            loan_type = [loan_type for loan_type in loan_type]
            state = queryset.values_list('state', flat=True).distinct()
            state = [state for state in state]

            print("Loaded filter in: ",(datetime.now()-pretime).total_seconds())

            
            filter_context = {
                'Paid status': paid_status,
                'Zone': zone,
                'Month': month,
                'Loan type': loan_type,
                'State': state,
            }

            filter_cc = dumps(filter_context)
            context = {
                'filter_context' : filter_context,  
                'filter_cc': filter_cc,
            }
            paid_status_post = values.get('Paid status', [])
            zone_post = values.get('Zone', [])
            month_post = values.get('Month', [])
            loan_type_post = values.get('Loan type', [])
            state_post = values.get('State', [])
            
            if paid_status_post:
                queryset = queryset.filter(paid_status__in=paid_status_post)

            if zone_post:
                queryset = queryset.filter(zone__in=zone_post)
            
            if month_post:
                queryset = queryset.filter(month__in=month_post)
            
            if loan_type_post:
                queryset = queryset.filter(product__in=loan_type_post)
            
            if state_post:
                queryset = queryset.filter(state__in=state_post)
            
            pretime = datetime.now()
            allocation = queryset.count()
            paid_count = queryset.filter(paid_status='Paid').count()
            print("Allocation: ",allocation)
            if allocation == 0 :
                connection_percentage = 0
                resolution_percentage = 0
                avg_attempt_intensity = 0
                avg_connect_intensity = 0
            else:
                connected = queryset.filter(callstatus='Connected').count()
                connection_percentage = (connected/allocation)*100
                resolution_percentage  = (paid_count/allocation)*100
                tot_attempt = queryset.aggregate(total_attempt=Sum('noofattempt'))
                avg_attempt_intensity = tot_attempt['total_attempt']/allocation
                tot_connect = queryset.aggregate(total_connect=Sum('noofconnect'))
                avg_connect_intensity = tot_connect['total_connect']/allocation


            pretime = datetime.now()
            month_percentage = queryset.values_list('month').annotate(count=Count('id'))
            month_counts = [count for month,count in month_percentage]
            month = ["-".join(month.split("'")) for month,count in month_percentage]
            if allocation == 0:
                percentage_list = [0 for count in month_counts]
            else:                
                percentage_list = [(count/allocation)*100 for count in month_counts]

            zone_values = queryset.values_list('zone').annotate(count=Count('id'))
            zone_list = [zone for zone,count in zone_values]
            zone_counts = [count for zone,count in zone_values]
            print("Zone: ",zone_list,zone_counts)

            lang_values = queryset.values_list('language').annotate(count=Count('id'))
            lang_list = [lang for lang,count in lang_values]
            lang_counts = [count for lang,count in lang_values]
            print(lang_list,lang_counts)

            connect_attempt = queryset.values_list('paid_status').annotate(count=Sum('noofconnect'),count1=Sum('noofattempt'))
            print(connect_attempt)
            connect_values = [connect for paid_status,connect,attempt in connect_attempt ]
            attempt_values = [attempt for paid_status,connect,attempt in connect_attempt ]
            print(connect_values,attempt_values);

            Loan_radar = queryset.values_list('product','paid_status').annotate(count=Count('id'))
            #loan_count = my_table.objects.using('mysql_db').values_list('product').annotate(count=Count('id'))
            #loan_count = { loan:count for loan,count in loan_count}
            print(Loan_radar)
            loan_list = []
            loan_paid = []
            loan_unpaid = []
            for i in range(len(Loan_radar)):
                if Loan_radar[i][0] not in loan_list:
                    loan_list.append(Loan_radar[i][0])
                if Loan_radar[i][1] == 'Paid' and (len(loan_list)-1) == len(loan_paid):
                    loan_paid.append(Loan_radar[i][2])
                elif Loan_radar[i][1] == 'Unpaid' and (len(loan_list)-1) == len(loan_unpaid):
                    loan_unpaid.append(Loan_radar[i][2])
                    
            print(loan_list,loan_paid,loan_unpaid)

            State_count = queryset.values_list('state','paid_status').annotate(count=Count('id'))
            state_list = []
            state_paid = []
            state_unpaid = []
            for i in State_count:
                if i[0] not in state_list:
                    state_list.append(i[0])
                if i[1] == 'Paid' and (len(state_list)-1) == len(state_paid):
                    state_paid.append(i[2])
                elif i[1] == 'Unpaid' and (len(state_list)-1) == len(state_unpaid):
                    state_unpaid.append(i[2])
            print(state_list,state_paid,state_unpaid)

            print("Total Time: ",(datetime.now()-pretime1).total_seconds())

            
            context = {
                'pie_month_list': month,
                'pie_percentage_list': percentage_list,
                'line_lang_list' : lang_list,
                'line_lang_counts' : lang_counts,
                'line_zone_list' : zone_list,
                'line_zone_counts' : zone_counts,
                'stacked_connect_values' : connect_values,
                'stacked_attempt_values' : attempt_values,
                'radar_loan_list' : loan_list,
                'radar_loan_paid' : loan_paid,
                'radar_loan_unpaid' : loan_unpaid,
                'state_list' : state_list,
                'state_paid' : state_paid,
                'state_unpaid' : state_unpaid,
            }

            piejson_context  = dumps(context)

            if 'Month' in values:
                month = values['Month']
                month = ["-".join(i.split("'")) for i in month]
                values['Month'] = month

            context = {
                    'allocation' : locale.format_string("%d",allocation, grouping=True),
                    'connect_percentage': round(connection_percentage,2),
                    'paid_count' : locale.format_string("%d",paid_count, grouping=True),
                    'resolution_percentage' : round(resolution_percentage,2),
                    'avg_attempt_intensity' : round(avg_attempt_intensity,2),
                    'avg_connect_intensity' : round(avg_connect_intensity,2),
                    'datajson_context': piejson_context,
                'filter_context' : filter_context,  
                'filter_cc': filter_cc,
                'Values': dumps(values),
            }
            print(values)

            # filter_context = {
            #     'Paid status': paid_status,
            # }
            # filter_cc = dumps(filter_context)
            # context = {
            #     'filter_context' : filter_context,  
            #     'filter_cc': filter_cc,
            #     'Values': dumps(values),
            # }

            
            return render(request, 'dashboard_using_python.html', context=context)
            
        else:
            return redirect('Main_app:login')
class pythonDashboardView(TemplateView):

    def get(self, request, **kwargs):
        if request.user.is_authenticated==True:

            
            pretime1 = datetime.now()
            pretime = pretime1
            paid_status = my_table.objects.using('mysql_db').values_list('paid_status', flat=True).distinct()
            paid_status = [paid_status for paid_status in paid_status]
            zone = my_table.objects.using('mysql_db').values_list('zone', flat=True).distinct()
            zone = [zone for zone in zone]
            month = my_table.objects.using('mysql_db').values_list('month', flat=True).distinct()
            month = ["-".join(month.split("'")) for month in month]
            loan_type = my_table.objects.using('mysql_db').values_list('product', flat=True).distinct()
            loan_type = [loan_type for loan_type in loan_type]
            state = my_table.objects.using('mysql_db').values_list('state', flat=True).distinct()
            state = [state for state in state]
            print("Loaded filter in: ",(datetime.now()-pretime).total_seconds())

            pretime = datetime.now()
            allocation = my_table.objects.using('mysql_db').count()
            if allocation == 0 :
                allocation = 0.000001
            print("allcation Loaded in: ",(datetime.now()-pretime).total_seconds())
            connected = my_table.objects.using('mysql_db').filter(callstatus='Connected').count()
            connection_percentage = (connected/allocation)*100
            paid_count = my_table.objects.using('mysql_db').filter(paid_status='Paid').count()
            resolution_percentage  = (paid_count/allocation)*100
            tot_attempt = my_table.objects.using('mysql_db').aggregate(total_attempt=Sum('noofattempt'))
            avg_attempt_intensity = tot_attempt['total_attempt']/allocation
            tot_connect = my_table.objects.using('mysql_db').aggregate(total_connect=Sum('noofconnect'))
            avg_connect_intensity = tot_connect['total_connect']/allocation
            print("Cards Updated in: ",(datetime.now()-pretime).total_seconds())

            pretime = datetime.now()
            allocation = my_table.objects.using('mysql_db').count()
            monthyy = my_table.objects.using('mysql_db').values_list('month').annotate(count=Count('id'))
            month_counts = [count for month,count in monthyy]
            month_list = ["-".join(month.split("'")) for month,count in monthyy]
            percentage_list = [(count/allocation)*100 for count in month_counts]
            zone_values = my_table.objects.using('mysql_db').values_list('zone').annotate(count=Count('id'))
            zone_list = [zone for zone,count in zone_values]
            zone_counts = [count for zone,count in zone_values]
            print("Zone: ",zone_list,zone_counts)

            lang_values = my_table.objects.using('mysql_db').values_list('language').annotate(count=Count('id'))
            lang_list = [lang for lang,count in lang_values]
            lang_counts = [count for lang,count in lang_values]
            print("Lang: ",lang_list,lang_counts)

            connect_attempt = my_table.objects.using('mysql_db').values_list('paid_status').annotate(count=Sum('noofconnect'),count1=Sum('noofattempt'))
            print(connect_attempt)
            connect_values = [connect for paid_status,connect,attempt in connect_attempt ]
            attempt_values = [attempt for paid_status,connect,attempt in connect_attempt ]
            print(connect_values,attempt_values);

            Loan_radar = my_table.objects.using('mysql_db').values_list('product','paid_status').annotate(count=Count('id'))
            loan_count = my_table.objects.using('mysql_db').values_list('product').annotate(count=Count('id'))
            loan_count = { loan:count for loan,count in loan_count}
            print(Loan_radar)
            loan_list = []
            loan_paid = []
            loan_unpaid = []
            for i in range(len(Loan_radar)):
                if Loan_radar[i][0] not in loan_list:
                    loan_list.append(Loan_radar[i][0])
                if Loan_radar[i][1] == 'Paid' and (len(loan_list)-1) == len(loan_paid):
                    loan_paid.append(round(100*(Loan_radar[i][2]/loan_count[Loan_radar[i][0]])))
                elif Loan_radar[i][1] == 'Unpaid' and (len(loan_list)-1) == len(loan_unpaid):
                    loan_unpaid.append(round(100*(Loan_radar[i][2]/loan_count[Loan_radar[i][0]])))
                    
            print(loan_list,loan_paid,loan_unpaid)

            State_count = my_table.objects.using('mysql_db').values_list('state','paid_status').annotate(count=Count('id'))
            state_list = []
            state_paid = []
            state_unpaid = []
            for i in State_count:
                if i[0] not in state_list:
                    state_list.append(i[0])
                if i[1] == 'Paid' and (len(state_list)-1) == len(state_paid):
                    state_paid.append(i[2])
                elif i[1] == 'Unpaid' and (len(state_list)-1) == len(state_unpaid):
                    state_unpaid.append(i[2])
            print(state_list,state_paid,state_unpaid)

        
            print("Graph Updated in: ",(datetime.now()-pretime).total_seconds())
     
            filter_context = {
                'Paid status': paid_status,
                'Zone': zone,
                'Month': month,
                'Loan type': loan_type,
                'State': state,
            }

            filter_cc = dumps(filter_context)

            context = {
                'pie_month_list': month_list,
                'pie_percentage_list': percentage_list,
                'line_lang_list' : lang_list,
                'line_lang_counts' : lang_counts,
                'line_zone_list' : zone_list,
                'line_zone_counts' : zone_counts,
                'stacked_connect_values' : connect_values,
                'stacked_attempt_values' : attempt_values,
                'radar_loan_list' : loan_list,
                'radar_loan_paid' : loan_paid,
                'radar_loan_unpaid' : loan_unpaid,
                'state_list' : state_list,
                'state_paid' : state_paid,
                'state_unpaid' : state_unpaid,
            }

            graphjson_context  = dumps(context)

            context = {
                'allocation' : locale.format_string("%d",allocation, grouping=True),
                'connect_percentage': round(connection_percentage,2),
                'paid_count' : locale.format_string("%d",paid_count, grouping=True),
                'resolution_percentage' : round(resolution_percentage,2),
                'avg_attempt_intensity' : round(avg_attempt_intensity,2),
                'avg_connect_intensity' : round(avg_connect_intensity,2),
                'datajson_context': graphjson_context,
                  'filter_context' : filter_context,
                  'filter_cc': filter_cc,
            }
            # filter_context = {
            #     'Paid status': paid_status,
            # }
            # filter_cc = dumps(filter_context)
            # context = {
            #     'filter_context' : filter_context,  
            #     'filter_cc': filter_cc,
            # }
            print("Total Time: ",(datetime.now()-pretime1).total_seconds())
            
            return render(request, 'dashboard_using_python.html', context=context)
        else:
            return redirect('Main_app:login')
    

    
            

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Main_app:home')
    template_name = 'registration/signup.html'

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if request.user.is_authenticated==False:
            return redirect('Main_app:login')
        else:
            return render(request, 'home.html', context=None)

#load data

class loading(TemplateView):
    template_name = 'loading.html'

class loading_put(TemplateView):
    def post(self, request, **kwargs):
        if request.user.is_authenticated==True:
            global values
            values = json.loads(request.body)
            print(values)
            return render(request, 'loading_put.html', context=None)
        else:
            return redirect('Main_app:login')
        
    def get(self, request, **kwargs):
        if request.user.is_authenticated==True:
            return render(request, 'loading_put.html', context=None)
        else:
            return redirect('Main_app:login')