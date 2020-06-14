import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from adjustText import adjust_text
import csv


def plot_in_vs_out_degree(filepath):
    """
     plots the in-degree vs out-degree of our network and saves the plot into a file
    :param filepath: the filepath in which we want to save our png plot
    """
    data_file_path = "node_properties_nba_analysis.csv" ## this file was generated from gephi. I simply exported the data from gephi into a csv
    df = pd.read_csv(data_file_path)
    ax = df.set_index('outdegree')['indegree'].plot(style='o')
    texts = []
    def label_point(outdegree, indegree, Label, ax):
        a = pd.concat({'outdegree': outdegree, 'indegree': indegree, 'Label': Label}, axis=1)
        for i, point in a.iterrows():
            #only include labels for players with >= 90 followers
            if point['indegree'] >= 90:
                texts.append(plt.text(x=point['outdegree'], y=point['indegree'], s=str(point['Label'])))
    label_point(df.outdegree, df.indegree, df.Label, ax)
    adjust_text(texts, arrowprops=dict(arrowstyle="->", color='b'))
    plt.title("Plot of follower count vs following count amongst NBA players")
    plt.xlabel("following count in NBA")
    plt.ylabel("follower count in NBA")
    # plt.show()
    plt.savefig(filepath)


def create_networkx_graph_from_edge_list_csv():
    """
    creates a networkX digraph based on the data in our nba network
    :return:
    """
    graph = nx.DiGraph()
    with open("overallNBANetwork.csv", "r", newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)  # move the reader cursor to next line
        # extracting each data row one by one
        for row in csvreader:
            graph.add_edge(row[0], row[1])
    return graph



plot_in_vs_out_degree(filepath="visualizations/indegree_vs_outdegree.png")

# use this graph object + networkx to do any additional graph analysis you might want
# most of my analysis was actually done in gephi
graph = create_networkx_graph_from_edge_list_csv()




