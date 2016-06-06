from pyquery import PyQuery as pq

p = pq('<p id="hello" class="hello"></p>')('p')
print p.addClass('beauty')
print p.removeClass('hello')
print p.css('font-size', '16px')
print p.css({'background-color': 'yellow'})
