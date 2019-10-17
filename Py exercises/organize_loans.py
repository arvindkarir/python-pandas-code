
def organize_loans(all_loans, outfile):

	for country in all_loans.keys():
		country_total = 0
		num_loans = 0
		for loan in all_loans[country]:
			num_loans += 1
			country_total += loan.cancelled - loan.principle

		print(country, "got {nloans} loans(s) with $".format(num_loans), country_total)
		for loan in all_loans[country]:
			print('\tID: {id}, Project: {proj}, loan amount: {amt}'.format(id=loan.id, proj=loan.project, amt=(loan.cancelled - loan.principal)))

		
