
#import inspect
#lines = inspect.getsource(calc_salary_julia)
#print(lines)


# def calc_salary_julia(month_df):
# 	# julia
# 	month = month_df.head(1).index.month[0]
# 	year = month_df.head(1).index.year[0]
# 	num_days_in_month = monthrange(year,month)[1]
# 	julia_salary_monthly = 31800
# 	sgi_year = 31800*12
# 	julia_pwc_kr_per_day = ((sgi_year*0.8*0.97) + (sgi_year*0.2*0.5))/365
# 	julia_p_kr_per_day = ((sgi_year*0.8*0.97))/365
# 	vacation_kr_per_day = (julia_salary_monthly*0.0043)
	
# 	## variables
# 	num_vacation_days = sum(month_df['vacation_j']*month_df['workday'])
# 	all_parent_days_j = month_df[['pwc_day','parent_day_j']].max(axis=1)
# 	num_total_parent_days = sum(all_parent_days_j)
# 	num_pwc = sum(month_df['pwc_day'])
# 	num_p_j = sum(month_df['parent_day_j'])
	
# 	# decide removal of salary
# 	if (num_total_parent_days==num_days_in_month):
# 		remove_from_salary_julia = julia_salary_monthly
# 	else:
# 		remove_from_salary_julia = ((31800*12)/365)*sum(all_parent_days_j)
# 	#decide money from FK
# 	from_fk_j = num_pwc*julia_pwc_kr_per_day + julia_p_kr_per_day*num_p_j
# 	total_salary = from_fk_j + julia_salary_monthly - remove_from_salary_julia + num_vacation_days*vacation_kr_per_day
# 	return total_salary

# def calc_salary_filip(month_df):
# 	# filip
# 	month = month_df.head(1).index.month[0]
# 	year = month_df.head(1).index.year[0]
# 	num_days_in_month = monthrange(year,month)[1]
# 	filip_salary_monthly = 42000
# 	sgi_year = filip_salary_monthly*12
# 	bb_10 = 46500*10
# 	salary_over_10bb_yearly = (filip_salary_monthly*12)-bb_10
# 	salary_below_10bb_yearly = filip_salary_monthly*12 - salary_over_10bb_yearly
# 	filip_klarna_kr_per_day = ((salary_below_10bb_yearly*0.8*0.97) + (salary_below_10bb_yearly*0.2)+ (salary_over_10bb_yearly))/365
# 	filip_p_kr_per_day = ((sgi_year*0.8*0.97))/365
# 	vacation_kr_per_day = (filip_salary_monthly*0.0043)
# 	## variables
# 	num_vacation_days = sum(month_df['vacation_f']*month_df['workday'])
# 	all_parent_days_filip = month_df[['klarna_day','parent_day_f','10d_f']].max(axis=1)
# 	num_total_parent_days = sum(all_parent_days_filip.multiply(month_df['mult_f']))
# 	num_klarna = sum(month_df['klarna_day'])
# 	#num_p_filip = sum(month_df[['parent_day_f','10d_f']].max(axis=1))
# 	fk_days_multiplier = month_df['mult_f']
# 	# decide removal of salary
# 	remove_from_salary_filip=0
# 	if (sum(all_parent_days_filip)==num_days_in_month):
# 		remove_from_salary_filip = filip_salary_monthly
# 	else:
# 		remove_from_salary_filip = ((filip_salary_monthly*12)/365)*sum(all_parent_days_filip)

# 	from_fk_filip = filip_p_kr_per_day*num_total_parent_days
# 	from_klarna_bonus = num_klarna*filip_klarna_kr_per_day
# 	total_salary = from_fk_filip + from_klarna_bonus + filip_salary_monthly - remove_from_salary_filip + num_vacation_days*vacation_kr_per_day	
# 	return total_salary








# data = data.fillna(0)

# # Julia lågbetald	1 561 kr
# # Julia medelbetald	2 192 kr
# # Julia högbetald	2 297 kr
# # Filip lågbetald	1 225 kr
# # Filip medelbetald	2 034 kr
# # Filip högbetald	2 397 kr






































# v_f = {}
# v_j = {}

# for d in big_cal:
# 	day = d.strftime('%Y-%m-%d')
# 	if not cal.is_working_day(d):
# 		v_f[day] = (100)
# 		v_j[day] = (80)
# 	else:
# 		v_f[day] = (0)
# 		v_j[day] = (0)


# def calculate_total_vacation_days(dict_v):
# 	num_days = 0
# 	for d in dict_v:
# 		if (dict_v[d] == 1):
# 			if(cal.is_working_day(d)):
# 				num_days = num_days + 1
# 	return(num_days)



# print(calculate_total_vacation_days(hej))


# for d in hej:
# 	if (hej[d] == 1):
# 		print(hej[d])
# 		if(cal.is_working_day(d)):
# 			num_days = num_days = 1




# gain = np.transpose(np.array([[1561,2192,2297,1225,2034,2397]]))
# empty = np.zeros((len(big_cal),6))
# for i in range(0,6,1):
# 	empty[0,i] = 1

# np.matmul(a, b)

# np.matmul(empty,gain)