def number_to_month (month):
    if month in range(1, 13):
        list = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        return list[month-1].lower()
    else:
        return "error"
number_to_month(1)
