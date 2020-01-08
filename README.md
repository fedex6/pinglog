# pinglog
Llevar un registro automático y saber si estuvo caída la conexión en algún momento.

## Requerimientos basicos
Hay que instalar pingparsing (compatible con python 2 y 3), para eso se ejecuta:
```
pip install pingparsing
```

## Configurar el cron
Yo lo hago mediante crontab
```
crontab -e
```
Suponiendo que el archivo lo ponemos en la carpeta _/home/[USER]/bots/_ asi deberia estar el archivo
```
*/5 * * * *   python /home/[USER]/bots/check_internet.py
```
De esta manera, se va a ejecutar cada 5 minutos, todo el tiempo.

***

### Mejoras futuras
Es la primer version basica, en cuanto pueda hare uno que guarde la velocidad promedio y sea levantable (?) por una planilla de calculos.
