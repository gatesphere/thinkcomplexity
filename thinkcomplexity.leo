<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo (http://leoeditor.com/leo_toc.html) -->
<?xml-stylesheet ekr_test?>
<leo_file xmlns:leo="http://www.leo-editor.org/2011/leo" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="peckj.20131202081144.4700"><vh>Chapter 1</vh>
<v t="peckj.20131202081144.4711"><vh>Simplified schelling model</vh>
<v t="peckj.20131202081144.4712"><vh>&lt;&lt; imports &gt;&gt;</vh></v>
<v t="peckj.20131202081144.4713"><vh>&lt;&lt; declarations &gt;&gt;</vh></v>
<v t="peckj.20131202081144.4714"><vh>create_city</vh></v>
<v t="peckj.20131202081144.4715"><vh>clear_city_tab</vh></v>
<v t="peckj.20131202081144.4716"><vh>print_city</vh></v>
<v t="peckj.20131202081144.4717"><vh>iterate</vh></v>
<v t="peckj.20131202081144.4718"><vh>cell_is_happy</vh></v>
<v t="peckj.20131202081144.4719"><vh>main</vh></v>
</v>
</v>
<v t="peckj.20131202081144.4701" a="E"><vh>Chapter 2</vh>
<v t="peckj.20131202081144.4720"><vh>@file GraphCode.py</vh></v>
<v t="peckj.20131202081144.4747" a="E"
expanded="peckj.20131202081144.4755,"><vh>@file Graph.py</vh></v>
<v t="peckj.20131202180255.3707"><vh>@file GraphWorld.py</vh></v>
<v t="peckj.20131202180255.3742" a="E"><vh>@file GraphTest.py</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="peckj.20131202081144.4700"></t>
<t tx="peckj.20131202081144.4701"></t>
<t tx="peckj.20131202081144.4711">@language python

&lt;&lt; imports &gt;&gt;
&lt;&lt; declarations &gt;&gt;

@others

main()</t>
<t tx="peckj.20131202081144.4712">import random</t>
<t tx="peckj.20131202081144.4713">neighborhood = 2 # cells on both sides
happy = 2 # at least this many cells are same

empty = .1
red = .45
blue = .45

numcells = 50
trials = 1000
</t>
<t tx="peckj.20131202081144.4714">def create_city(n):
  city = []
  for i in range(n):
    x = random.random()
    if x &lt; empty:
      cell = ' '
    elif x &lt; empty+red:
      cell = '+'
    else:
      cell = '.'
    city.append(cell)
  return city
</t>
<t tx="peckj.20131202081144.4715">def clear_city_tab():
  g.app.log.deleteTab('City')</t>
<t tx="peckj.20131202081144.4716">def print_city(city):
  tab='City'
  g.es(''.join(city),tabName=tab, color='darkgreen')</t>
<t tx="peckj.20131202081144.4717">def iterate(city):
  # choose random cell
  cell = random.randint(0, len(city)-1)
  # determine if happy
  # if so, do nothing
  if not cell_is_happy(cell, city):
    # else, move to random empty cell
    empties = [x for x in range(len(city)) if city[x] == ' ']
    destination = empties[random.randint(0, len(empties)-1)]
    city[destination] = city[cell]
    city[cell] = ' '</t>
<t tx="peckj.20131202081144.4718">def cell_is_happy(cell, city):
  # cell is an index into city
  type = city[cell]
  count = 0
  for i in range(1, neighborhood+1):
    if city[cell-i] == type: count += 1
    if cell+i &gt;= len(city):
      if city[len(city)-cell+i] == type: count += 1
    else:
      if city[cell+i] == type: count += 1
  return count &gt;= happy</t>
<t tx="peckj.20131202081144.4719">def main():
  clear_city_tab()
  city = create_city(numcells)
  print_city(city)
  for i in range(trials):
    iterate(city)
    print_city(city)
  g.es('Done', tabName='City')
    </t>
</tnodes>
</leo_file>
