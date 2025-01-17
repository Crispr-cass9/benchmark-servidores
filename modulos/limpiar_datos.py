import subprocess



def realizar_pruebas(enlace, cantidad_peticiones, concurrencia, cantidad_pruebas):

    resultados=[]

    for i in range(cantidad_pruebas):

        command = f'ab -n {cantidad_peticiones} -c {concurrencia} {enlace}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

        output = process.communicate()[0].decode().split('\n')
        print(output)
        datos = {x.split(':')[0].strip() : x.split(':')[-1].strip() for x in output[7:] if x != ''}
        print(datos)

        lista_valores = []
        for valor in datos['Connect'].split(' '):

            if valor != '':
                lista_valores.append(valor.strip())

        datos['Connect'] = lista_valores


        lista_valores = []
        for valor in datos['Processing'].split(' '):

            if valor != '':
                lista_valores.append(valor.strip())

        datos['Processing'] = lista_valores


        lista_valores = []
        for valor in datos['Waiting'].split(' '):

            if valor != '':
                lista_valores.append(valor.strip())

        datos['Waiting'] = lista_valores

        lista_valores = []
        for valor in datos['Total'].split(' '):

            if valor != '':
                lista_valores.append(valor.strip())

        datos['Total'] = lista_valores

        datos['Orden Peticion'] = i
        resultados.append(datos)

    return resultados






#     connection_times = [[x.strip() for x in line.split(' ') if x != ''] for line in datos[17:21]]
#     connection_times = {'Connect': connection_times[0], 'Processing':connection_times[1], 'Waiting': connection_times[2], 'Total': connection_times[3]}

#     percentages = [[x for x in line.split(' ') if x != ''] for line in datos[22:]]
#     percentages_object= {}

#     for dato in percentages:
#         percentages_object[dato[0]] = dato[1]
    

#     data_list = datos[:15]
#     data_list.append(connection_times)
#     data_list.append(percentages)
#     objeto = peticion_individual(*data_list)
#     tests.append(objeto)

# medias = {
#     'length': 0,
#     'concurrency': 0,
#     'time_for_test': 0,
#     'complete_requests': 0,
#     'failed_requests': 0,
#     'total_transferred': 0,
#     'html_transferred': 0,
#     'requests_per_second': 0,
#     'time_per_request': 0,
#     'time_per_request2': 0,
#     'transfer_rate': 0,
#     'connection_times': {'connect':[0, 0, 0, 0, 0], 'processing': [0, 0, 0, 0, 0], 'waiting': [0, 0, 0, 0, 0], 'total': [0, 0, 0, 0, 0]},
#     'Percentage': {'50%': 0, '66%': 0, '75%': 0, '80%': 0, '90%': 0, '95%': 0, '98%': 0, '99%': 0, '100%': 0}
# }
# for test in tests:
#     print(test.length)
#     medias['length']+= float(test.length.split(' ')[1])
#     medias['concurrency']+= float(test.concurrency)
#     medias['time_for_test']+= float(test.time_for_test)
#     medias['complete_requests'] += float(test.complete_requests)
#     medias['failed_requests']+= float(test.failed_requests)
#     medias['total_transferred']+= float(test.total_transferred)
#     medias['html_transferred']+= float(test.html_transferred)
#     medias['requests_per_second']+= float(test.requests_per_second)
#     medias['time_per_request']+= float(test.time_per_request)
#     medias['time_per_request_2']+= float(test.time_per_request_2)
#     medias['transfer_rate']+= float(test.transfer_rate)

#     for clave, valor in test.connection_times.items():
#         for index, datos in enumerate(valor):
#             medias[clave][index] = datos
#     medias['percentages']+= test.percentages

# print(medias)