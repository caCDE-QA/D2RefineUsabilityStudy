from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles, venn3_unweighted

colors = ('#000000', '#828282', '#cecece')
alpha = 0.5

def draw_example_venn():
    plt.figure()

    data = (1,1,1,1,1,1,1)

    v = venn3(subsets=data, alpha=alpha, set_colors=colors, set_labels=["Activity Model\n(In Use)", "User Model\n(Wanted)", "Designer Model\n(Implemented)"])

    v.get_label_by_id('100').set_text('')
    v.get_label_by_id('010').set_text('')
    v.get_label_by_id('001').set_text('')
    v.get_label_by_id('111').set_text('')
    v.get_label_by_id('110').set_text('')
    v.get_label_by_id('011').set_text('')
    v.get_label_by_id('101').set_text('')

    plt.annotate('Implemented\nWanted\nIn Use $\checkmark$', xy=v.get_label_by_id('100').get_position() - np.array([0, 0.05]), xytext=(-60,-60),
                 ha='left', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=1),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.annotate('Implemented\nWanted $\checkmark$\nIn Use', xy=v.get_label_by_id('010').get_position() - np.array([0, 0.05]), xytext=(60,-60),
                 ha='left', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=1),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.annotate('Implemented $\checkmark$\nWanted\nIn Use', xy=v.get_label_by_id('001').get_position() - np.array([0, 0.05]), xytext=(-160,-60),
                 ha='left', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=1),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.annotate('Implemented $\checkmark$\nWanted $\checkmark$ \nIn Use $\checkmark$', xy=v.get_label_by_id('111').get_position() - np.array([0, 0.05]), xytext=(60,65),
                 ha='left', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=1),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.annotate('Implemented\nWanted $\checkmark$ \nIn Use $\checkmark$', xy=v.get_label_by_id('110').get_position() - np.array([0, 0.05]), xytext=(-40,60),
                 ha='left', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=1),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.annotate('Implemented$\checkmark$\nWanted $\checkmark$\nIn Use', xy=v.get_label_by_id('011').get_position() - np.array([0, 0.05]), xytext=(60,-60),
                 ha='left', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=1),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.annotate('Implemented $\checkmark$\nWanted\nIn Use $\checkmark$', xy=v.get_label_by_id('101').get_position() - np.array([0, 0.05]), xytext=(-60,-60),
                 ha='left', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=1),
                 arrowprops=dict(arrowstyle='->', color='black'))

    plt.savefig('figures/models.png')

def draw_venn(labels, data, totals):
    figure, axes = plt.subplots(1, 3)
    figure.set_size_inches(12, 4)

    axes[0].set_title('D2Refine', y=1.08, fontsize=14, fontweight='bold')
    axes[1].set_title('OntoMaton', y=1.08, fontsize=14, fontweight='bold')
    axes[2].set_title('RightField', y=1.08, fontsize=14, fontweight='bold')

    #plt.suptitle('Function Distribution')

    def font(out):
        for text in out.set_labels:
            text.set_horizontalalignment("center")

    font(venn3_unweighted(subsets=data[0], alpha=alpha, set_labels=labels, ax=axes[0]))

    font(venn3_unweighted(subsets=data[1], alpha=alpha, set_labels=labels, ax=axes[1]))

    font(venn3_unweighted(subsets=data[2], alpha=alpha, set_labels=labels, ax=axes[2]))

    plt.savefig('figures/models_venn.png')

