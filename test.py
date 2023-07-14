class DrugAnalyzer:
    def __init__(self, data) -> None:
        self.data = data
    def __add__(self, x):
        if (len(x)!=4):
            raise ValueError("Improper length of the added list.")
        else:
            self.data.append(x)
            return self            
    def verify_series(self, series_id: str, act_subst_wgt: float, act_subst_rate: float, allowed_imp: float) -> bool:
        pills=[]
        impurities = pill_wgt = overall_active_sustances =0
        pills_parameters=False
        pills = [substring for substring in self.data if series_id in substring[0]]

        if not pills:
            raise ValueError(f"{series_id} series is not present within the dataset.")
        else:            
            pill_wgt, overall_active_sustances, impurities = [sum(i) for i in list(zip(*pills))[1:]]                       
            total_act_subst_wgt=len(pills)*act_subst_wgt
            allowed_rate=act_subst_rate*total_act_subst_wgt
            if (total_act_subst_wgt-allowed_rate) <= overall_active_sustances <= (total_act_subst_wgt+allowed_rate)  and impurities<pill_wgt*allowed_imp:
                pills_parameters=True

        return pills_parameters


my_drug_data = [['L01-10', 1007.67, 102.88, 1.00100],['L01-06', 996.42, 99.68, 2.00087],['G02-03', 1111.95, 125.04, 3.00100],['G03-06', 989.01, 119.00, 4.00004] ]

my_analyzer = DrugAnalyzer(my_drug_data)

print(my_analyzer.data)

my_new_analyzer = my_analyzer + ['G03-01', 789.01, 129.00, 0.00008]
print(my_new_analyzer.data)

#my_new_analyzer = my_analyzer + ['G03-01', 129.00, 0.00008]

#print(my_new_analyzer.data)

my_drug_data = [['L01-10', 1000.02, 102.88, 1.00100],['L01-06', 999.90, 96.00, 2.00087],['G02-03', 1000, 96.50, 3.00100],['G03-06', 989.01, 119.00, 4.00004]]

my_analyzer = DrugAnalyzer(my_drug_data)

print(my_analyzer.verify_series(series_id = 'L01', act_subst_wgt = 100, act_subst_rate = 0.05, allowed_imp = 0.01))


"""
class DrugAnalyzer:
    def __init__(self, data) -> None:
        self.data = data

    def __add__(self, x) :
        
        if (len(x)==4):
            
            self.data.append(x)
            return self
            
        else:
            
            raise ValueError("Improper length of the added list.")

    def verify_series(self, series_id: str, act_subst_wgt: float, act_subst_rate: float, allowed_imp: float) -> bool:
        
        drug_flag=False
        pills=[]
        
        for drug in self.data:
            
            if drug[0][:3] == series_id:
                drug_flag=True
                pills.append(drug)
        
        if drug_flag==False:
            
            raise ValueError(f"{series_id} series is not present within the dataset.")
        else:
            
            pills_parameters=False
            overall_active_sustances=0
            impurities=0
            pill_wgt=0
            
            for pill in pills:
                
                overall_active_sustances+=pill[2]
                impurities+=pill[3]
                pill_wgt+=pill[1]
            
            total_act_subst_wgt=len(pills)*act_subst_wgt
            allowed_rate=act_subst_rate*total_act_subst_wgt
            
            if overall_active_sustances< allowed_rate+total_act_subst_wgt and overall_active_sustances > total_act_subst_wgt-allowed_rate and impurities<pill_wgt*allowed_imp:
                
                pills_parameters=True


            return pills_parameters
"""