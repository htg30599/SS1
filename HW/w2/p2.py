def main():
    list_month = ['January', 'February', 'March',
                  'April', 'May', 'June', 'July',
                  'August', 'September', 'October',
                  'November', 'December']
    date_str = input("Enter date in the type: mm/dd/yy:")
    date_lst = date_str.split("/")
    month_num = int(date_lst[0])
    day = date_lst[1]
    year = date_lst[2]

    month_name = list_month[month_num - 1]

    l_date = month_name + " " + day + " " + year
    print(l_date)


main()
