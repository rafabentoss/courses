segundos_str = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias=segundos_str//86400
segs_restantes1=segundos_str%86400
horas=segs_restantes1//3600
segs_restantes2=segs_restantes1%3600
minutos=segs_restantes2//60
segs_restantes_final=segs_restantes2%60

print(dias,"dias,",horas, "horas,",minutos, "minutos e", segs_restantes_final, "segundos.")