#Take the input of all the ice cream bars

june = int(input("Enter the number of bars ordered in June: "))
july = int(input("Enter the name of bars ordered in July: "))
august = int(input("Enter the name of bars ordered in August: "))


sum_of_bars = june + july + august   #Add all the bars 
bars_half = sum_of_bars/2            #Half the sum of the bar

small_boxes = round(bars_half/5)     #Number of bars per small box
large_boxes = round(bars_half/20)    #Number of bars per large box
 
#Output of the Small & Large boxes 
print("Number of small boxes {}" .format(small_boxes))
print("Number of large boxes {}".format(large_boxes))

#Percentage Markup of 90% for small boxes
percentage_markup_june_small = ((90/100)*0.50) + 0.50 
percentage_markup_july_small = ((90/100)*1.00) + 1.00
percentage_markup_august_small = ((90/100)*0.75) + 0.75

#Calculating all the marked up price of the small boxes
small_price_june = june * percentage_markup_june_small
small_price_july = july * percentage_markup_july_small
small_price_august= august * percentage_markup_august_small

small_box_price = small_price_june + small_price_july + small_price_august #Adding the marked up prices
selling_price = (small_box_price/sum_of_bars)*5 #Calculation to find the Selling price of the Small box
selling_price_final_small = round(selling_price, 2) #Getting the Selling Price for the Small box

#Output of Selling prices per small box
print("Selling Price Per Small Box ${}" .format(selling_price_final_small))


#Percentage Markup of 80% for big boxes
percentage_markup_june_large = ((80/100)*0.50) + 0.50 
percentage_markup_july_large = ((80/100)*1.00) + 1.00
percentage_markup_august_large = ((80/100)*0.75) + 0.75

#Calculating all the marked up price of the large boxes
large_price_june = june * percentage_markup_june_large  
large_price_july = july * percentage_markup_july_large
large_price_august= august * percentage_markup_august_large


large_box_price = large_price_june + large_price_july + large_price_august #Adding the marked up prices 
selling_price = (large_box_price/sum_of_bars)*20 #Calculation to find the Selling price of the large box
selling_price_final_large = round(selling_price, 2) #Getting the Selling Price for the large box

#Output of Selling price per large box
print("Selling Price Per Small Box ${}" .format(selling_price_final_large))
