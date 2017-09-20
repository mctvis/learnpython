def health_calc(age,apple,cigs):
    answer=(100-age)+(apple*3.5)-(cigs*2)
    print(answer)

buckys_data=[27,29,0]
health_calc(buckys_data[0],buckys_data[1],buckys_data[2])
health_calc(*buckys_data)#another way of sending data