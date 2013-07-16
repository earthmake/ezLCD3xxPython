import wmi
import psutil
import os
from visual.graph import *
from datetime import date
from visual.controls import *


graph1 = gdisplay(x=0,y=0 ,width=400, height=300,
xtitle='Interval', ytitle='Bytes',
foreground=color.green, background=color.black)
label(display=graph1.display, pos=(50000,100000000000), text="Network Monitoring")
graph1.display.visible = False # make the display invisible
now=date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
f1 = gcurve(color=color.cyan)
f2 = gcurve(color=color.red)
f3 = gcurve(color=color.blue)
f4 = gcurve(color=color.green)
       
graph2 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Percentage',
foreground=color.green, background=color.black)
label(display=graph2.display, pos=(50000,100), text="CPU and Temp Processor")
graph2.display.visible = False # make the display invisible
f5 = gcurve(color=color.red)
f6 = gcurve(color=color.yellow)

graph3 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Bytes',
foreground=color.green, background=color.black)
label(display=graph3.display, pos=(50000,100000000000), text="Bytes Memory Usage")
graph3.display.visible = False # make the display invisible
f7=gcurve(color=color.yellow)
f8=gcurve(color=color.red)

graph4 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Count',
foreground=color.green, background=color.black)
label(display=graph4.display, pos=(50000,100000000000), text="Read Count")
graph4.display.visible = False # make the display invisible
f9=gcurve(color=color.blue)
f10=gcurve(color=color.orange)

graph5 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Time',
foreground=color.green, background=color.black)
label(display=graph5.display, pos=(50000,10000000000), text="Read Time")
graph5.display.visible = False # make the display invisible
f11=gcurve(color=color.red)
f12=gcurve(color=color.yellow)

graph6 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Time',
foreground=color.green, background=color.black)
label(display=graph6.display, pos=(50000,10000000000), text="Read Time")
graph6.display.visible = False # make the display invisible
f13=gcurve(color=color.red)
f14=gcurve(color=color.yellow)
f15=gcurve(color=color.blue)
f16=gcurve(color=color.magenta)
f17=gcurve(color=color.green)

graph7 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Time',
foreground=color.green, background=color.black)
label(display=graph7.display, pos=(50000,10000000000), text="Read Time")
graph7.display.visible = False # make the display invisible
f18=gcurve(color=color.blue)
f19=gcurve(color=color.orange)
f20=gcurve(color=color.red)
f21=gcurve(color=color.magenta)
f22=gcurve(color=color.green)
f23=gcurve(color=color.cyan)

graph8 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Time',
foreground=color.green, background=color.black)
label(display=graph8.display, pos=(50000,10000000000), text="Read Time")
graph8.display.visible = False # make the display invisible
f24=gcurve(color=color.yellow)
f25=gcurve(color=color.blue)
f26=gcurve(color=color.red)
f27=gcurve(color=color.orange)

graph9 = gdisplay(x=0,y=0, width=400, height=300,xtitle='Interval', ytitle='Time',
foreground=color.green, background=color.black)
label(display=graph9.display, pos=(50000,10000000000), text="Read Time")
graph9.display.visible = False # make the display invisible
f28 = gcurve(color=color.cyan)
f29 = gcurve(color=color.red)
f30 = gcurve(color=color.blue)
f31 = gcurve(color=color.green)
f32=gcurve(color=color.yellow)
f33=gcurve(color=color.blue)
f34=gcurve(color=color.red)
f35=gcurve(color=color.orange)
f36 = gcurve(color=color.red)
f37 = gcurve(color=color.yellow)
f38=gcurve(color=color.yellow)
f39=gcurve(color=color.red)
f40=gcurve(color=color.blue)
f41=gcurve(color=color.orange)
f42=gcurve(color=color.red)
f43=gcurve(color=color.yellow)
f44=gcurve(color=color.red)
f45=gcurve(color=color.yellow)
f46=gcurve(color=color.blue)
f47=gcurve(color=color.magenta)
f48=gcurve(color=color.green)
f49=gcurve(color=color.blue)
f50=gcurve(color=color.orange)
f51=gcurve(color=color.red)
f52=gcurve(color=color.magenta)
f53=gcurve(color=color.green)
f54=gcurve(color=color.cyan)


for x in range(100000000):
  e=psutil.network_io_counters()
  d=e.bytes_sent
  f=e.bytes_recv
  g=e.packets_sent
  h=e.packets_recv
  dd=str(d)
  print d
  ff=str(f)
  print f
  gg=str(g)
  print g
  hh=str(h)
  print h
  p = psutil.Process(os.getpid())
  b = p.get_cpu_percent(interval=0.1)
  w=wmi.WMI(namespace="root\wmi")
  temperature_info=w.MSAcpi_ThermalZoneTemperature()[0]
  a=(temperature_info.CurrentTemperature/10)-273
  i=psutil.disk_io_counters()
  j=i.read_count
  k=i.write_count
  l=i.read_bytes
  m=i.write_bytes
  n=i.read_time
  o=i.write_time
  q=psutil.avail_phymem()
  r=psutil.used_phymem()
  s=psutil.total_virtmem()
  t=psutil.avail_virtmem()
  u=psutil.used_virtmem()
  v=psutil.disk_io_counters(perdisk=False)
  z=v.read_count
  z1=v.write_count
  z2=v.read_bytes
  z3=v.write_bytes
  z4=v.read_time
  z5=v.write_time
  z6=psutil.network_io_counters(pernic=False)
  z7=z6.bytes_sent
  z8=z6.bytes_recv
  z9=z6.packets_sent
  z10=z6.packets_recv
  f1.plot(pos=(x,d))
  dd=str(d)
  print d
  f2.plot(pos=(x,f))
  f3.plot(pos=(x,g))
  f4.plot(pos=(x,h))
  f5.plot(pos=(x,b))
  f6.plot(pos=(x,a))
  f7.plot(pos=(x,l))
  f8.plot(pos=(x,m))
  f9.plot(pos=(x,j))
  f10.plot(pos=(x,k))
  f11.plot(pos=(x,n))
  f12.plot(pos=(x,o))
  f13.plot(pos=(x,q))
  f14.plot(pos=(x,r))
  f15.plot(pos=(x,s))
  f16.plot(pos=(x,t))
  f17.plot(pos=(x,u))
  f18.plot(pos=(x,z))
  f19.plot(pos=(x,z1))
  f20.plot(pos=(x,z2))
  f21.plot(pos=(x,z3))
  f22.plot(pos=(x,z4))
  f23.plot(pos=(x,z5))
  f24.plot(pos=(x,z7))
  f25.plot(pos=(x,z8))
  f26.plot(pos=(x,z9))
  f27.plot(pos=(x,z10))
  f28.plot(pos=(x,d))
  dd=str(d)
  print d
  f29.plot(pos=(x,f))
  f30.plot(pos=(x,g))
  f31.plot(pos=(x,h))
  f32.plot(pos=(x,b))
  f33.plot(pos=(x,a))
  f34.plot(pos=(x,l))
  f35.plot(pos=(x,m))
  f36.plot(pos=(x,j))
  f37.plot(pos=(x,k))
  f38.plot(pos=(x,n))
  f39.plot(pos=(x,o))
  f40.plot(pos=(x,q))
  f41.plot(pos=(x,r))
  f42.plot(pos=(x,s))
  f43.plot(pos=(x,t))
  f44.plot(pos=(x,u))
  f45.plot(pos=(x,z))
  f46.plot(pos=(x,z1))
  f47.plot(pos=(x,z2))
  f48.plot(pos=(x,z3))
  f49.plot(pos=(x,z4))
  f50.plot(pos=(x,z5))
  f51.plot(pos=(x,z7))
  f52.plot(pos=(x,z8))
  f53.plot(pos=(x,z9))
  f54.plot(pos=(x,z10))
