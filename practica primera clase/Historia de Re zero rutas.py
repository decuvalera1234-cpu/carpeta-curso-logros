# inicio de la historia de subaru natsuki
print("\n" + "="*50)
print("Rutas de Re Zero")
print("="*50 + "\n")

print("🧑 Eres Subaru Natsuki")
print("Eres un tipo sin habilidades, ni nada de fuerza, ni poder")
print("Siendo teletransportado a otro mundo de repente\n")

# primera pregunta listo
print("¿Qué haces primero?\n")
print("OPCIONES: 1.VER ALREDEDORES | 2.HABLAR VENDEDOR | 3.QUEDARSE | 4.EXPLORAR CIUDAD")
respuesta1 = input("Elige tu camino: ").strip().upper()

if respuesta1 == "VER ALREDEDORES":
    #segunda pregunta Listo
    print("\nTe encuentras en un callejón sin salida y ves a tres ladrones.")
    print("OPCIONES: 1.LUCHAR | 2.GRITAR | 3.HABLAR | 4.HUIR")
    respuesta2 = input("Elige tu camino: ").strip().upper()
    
    if respuesta2 == "LUCHAR":
        #tercera pregunta Listo
        print("\nPeleas contra los ladrones. ¿A quién atacas primero?")
        print("OPCIONES: FLACO | GORDO | ENANO | DESARMADO")
        respuesta3 = input("Elige tu camino: ").strip().upper()
        
        if respuesta3 == "FLACO":
            #cuarta pregunta Listo
            print("\nLo golpeas desprevenido. Están aturdidos, ¿a quién atacas ahora?")
            print("OPCIONES: 1.GORDO | 2.ENANO | 3.ESCAPAR | 4.RENDERSE")
            respuesta4 = input("Elige tu camino: ").strip().upper()
            
            if respuesta4 == "GORDO":
                #quinta pregunta Listo
                print("\nDerribas al gordo. ¿Qué haces con el dinero que soltaron?")
                print("OPCIONES: 1.ROBAR | 2.DEJARLO | 3.BUSCAR GUARDIA | 4.ESCONDERSE")
                respuesta5 = input("Elige tu camino: ").strip().upper()
                
                if respuesta5 == "ROBAR":
                    #sexta pregunta Listo
                    print("\nTe llevas el dinero. ¿A dónde vas ahora?")
                    print("OPCIONES: 1.PUEBLO | 2.MERCADO | 3.BOSQUE | 4.TABERNA")
                    respuesta6 = input("Elige tu camino: ").strip().upper()
                    
                    if respuesta6 == "PUEBLO":
                        #sectima pregunta Listo
                        print("\nLlegas a un pueblo lejano. ¿En qué trabajas?")
                        print("OPCIONES: 1.CAMPESINO | 2.COMERCIANTE | 3.HERRERO | 4.PANADERO")
                        respuesta7 = input("Elige tu camino: ").strip().upper()
                        
                        if respuesta7 == "CAMPESINO":
                            #octava pregunta Listo
                            print("\nCompras una parcela. ¿Qué vas a sembrar?")
                            print("OPCIONES: 1.MANZANAS | 2.TRIGO | 3.PAPAS | 4.FLORES")
                            respuesta8 = input("Elige tu camino: ").strip().upper()
                            
                            if respuesta8 == "MANZANAS":
                                #novena pregunta Listo
                                print("\nTus manzanas son famosas. ¿A quién se las vendes?")
                                print("OPCIONES: 1.NOBLES | 2.ALDEA | 3.VIAJEROS | 4.EJÉRCITO")
                                respuesta9 = input("Elige tu camino: ").strip().upper()
                                
                                if respuesta9 == "NOBLES":
                                    #decima pregunta Listo
                                    print("\nUn noble te hace una oferta para comprar toda tu granja.")
                                    print("OPCIONES: 1.ACEPTAR | 2.RECHAZAR | 3.NEGOCIAR | 4.RETIRARSE")
                                    respuesta10 = input("Elige tu camino: ").strip().upper()
                                    
                                    if respuesta10 == "ACEPTAR":
                                        print("\nFin feliz: Te vuelves rico vendiendo tu granja y vives una vida tranquila.")
                                    elif respuesta10 == "RECHAZAR":
                                        print("\nEl noble se enfada y manda a destruir tu granja. Mueres.")
                                    elif respuesta10 == "NEGOCIAR":
                                        print("\nConsigues el doble de dinero y compras un castillo. Fin Excelente.")
                                    elif respuesta10 == "RETIRARSE":
                                        print("\nTe vas a otra ciudad con tus ahorros. Fin Pacífico.")
                                    else:
                                        print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")
                                
                                elif respuesta9 == "ALDEA":
                                    print("\nVives feliz en la aldea como el abastecedor local. Fin Corto.")
                                elif respuesta9 == "VIAJEROS":
                                    print("\nUn viajero resulta ser un asesino y te ataca. Retorno por muerte.")
                                elif respuesta9 == "EJÉRCITO":
                                    print("\nEl ejército te recluta a la fuerza y mueres en combate.")
                                else:
                                    print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")
                            
                            elif respuesta8 == "TRIGO":
                                print("\nUna plaga arruina tu cosecha y mueres de hambre. Retorno por Muerte.")
                            elif respuesta8 == "PAPAS":
                                print("\nConsigues suficiente alimento para vivir en paz.")
                            elif respuesta8 == "FLORES":
                                print("\nNadie compra flores y terminas en la ruina.")
                            else:
                                print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")
                        
                        elif respuesta7 == "COMERCIANTE":
                            print("\nTe va bien en los negocios pero te asaltan en el camino.")
                        elif respuesta7 == "HERRERO":
                            print("\nNo tienes fuerza para forjar metal y te despiden.")
                        elif respuesta7 == "PANADERO":
                            print("\nEl horno explota y mueres en el accidente.")
                        else:
                            print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")
                    
                    elif respuesta6 == "MERCADO":
                        print("\nLos guardias te ven el dinero robado y te arrestan.")
                    elif respuesta6 == "BOSQUE":
                        print("\nUnas bestias mágicas te emboscan en la noche.")
                    elif respuesta6 == "TABERNA":
                        print("\nGastas todo el dinero en una noche y terminas en la calle.")
                    else:
                        print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")
                
                elif respuesta5 == "DEJARLO":
                    print("\nEl dinero se lo queda otro ladrón y te quedas sin nada.")
                elif respuesta5 == "BUSCAR GUARDIA":
                    print("\nLos guardias te confunden con uno de los bandidos.")
                elif respuesta5 == "ESCONDERSE":
                    print("\nTe quedas atrapado en el callejón hasta que anochece.")
                else:
                    print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")

            elif respuesta4 == "ENANO":
                print("\nEl gordo alto te da un golpe y te estampa contra la pared. Mueres.")
            elif respuesta4 == "ESCAPAR":
                print("\nTropiezas al intentar correr y te atrapan.")
            elif respuesta4 == "RENDERSE":
                print("\nTe quitan todo y te dejan inconsciente.")
            else:
                print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")

        elif respuesta3 == "GORDO":
            print("\nEl flaco saca dos dagas y te apuñala por la espalda. Mueres.")
        elif respuesta3 == "ENANO":
            print("\nEl enano esquiva tu golpe y los otros dos te arrollan.")
        elif respuesta3 == "DESARMADO":
            print("\nIntentas desarmarlos pero no tienes experiencia en combate.")
        else:
            print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")

    elif respuesta2 == "GRITAR":
        print("\nNadie viene a ayudarte. Los ladrones te atacan y mueres.")
    elif respuesta2 == "HABLAR":
        print("\nIntentas razonar, pero los ladrones no escuchan y te golpean.")
    elif respuesta2 == "HUIR":
        print("\nEl callejón está bloqueado y no encuentras salida.")
    else:
        print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")

elif respuesta1 == "HABLAR VENDEDOR":
    print("\nEl vendedor te pregunta si tienes dinero para comprar algo...")
elif respuesta1 == "QUEDARSE":
    print("\nTu mente se corrompe y mueres por la desesperación.")
elif respuesta1 == "EXPLORAR CIUDAD":
    print("\nTe pierdes entre la multitud del Reino de Lugunica...")
else:
    print("Opción no válida, tu ruta ha terminado con la destrucción de tu mente.")