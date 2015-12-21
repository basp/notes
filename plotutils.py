import math

def arrowprops(dx, dy, **kwargs):
    m = math.sqrt(dx**2 + dy**2)
    l = 1/8 * m
    w = 2/3 * l
    return { 
        'head_length': kwargs.get('head_length', l), 
        'head_width': kwargs.get('head_width', w), 
        'length_includes_head': True, 
        'overhang': kwargs.get('overhang', 0.0),
        'fc': kwargs.get('fc', 'b'),
        'ec': kwargs.get('ec', 'b')
    }
    
def plot_rect(ax, p, fmt='b'):
    x, y = p
    ax.plot([0, x], [y, y], fmt) # horizontal line
    ax.plot([x, x], [0, y], fmt) # vertical line

def setup_axes(ax, **kwargs):
    ticklength = kwargs.get('ticklength', 15)
    tickwidth = kwargs.get('tickwidth', 1)
    tickdirection = kwargs.get('tickdirection', 'inout')
    xticks = kwargs.get('xticks', [])
    yticks = kwargs.get('yticks', [])
    xticklabels = kwargs.get('xticklabels', [])
    yticklabels = kwargs.get('yticklabels', [])
    ax.tick_params('both', length=ticklength, width=tickwidth, direction=tickdirection)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.xaxis.set_ticks(kwargs.get('xticks', xticks))
    ax.xaxis.set_ticklabels(kwargs.get('xticklabels', xticklabels))
    ax.yaxis.set_ticks(kwargs.get('yticks', yticks))
    ax.yaxis.set_ticklabels(kwargs.get('yticklabels', yticklabels))
    ax.xaxis.tick_bottom()
    ax.yaxis.tick_left()
    ax.set_xlim(*kwargs.get('xlim', (-1, 1)))
    ax.set_ylim(*kwargs.get('ylim', (-1, 1)))
    ax.set_aspect(1.0)