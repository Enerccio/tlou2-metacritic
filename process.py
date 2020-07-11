import pandas

READ_N_ROWS = 13000

data = pandas.read_csv("reviews.csv", names=["name", "date", "score", "review"], nrows=READ_N_ROWS, 
    dtype={"name": str, "date": str, "score": pandas.np.int32, "review": str})

# drop scrapped duplicates
data = data[~data.duplicated(subset=["name", "score", "review"], keep=False)]

print "Processing " + str(data.shape[0]) + " rows"
    
# check metacritic sanity
print "Score average (all) " + str(data["score"].mean().item())    

# drop 0
data0 = data[data['score'] > 0]
#drop 10
data10 = data[data['score'] < 10]
# both 0 and 10 dropped
data_remove_extremes = data[(data['score'] > 0) & (data['score'] < 10)]

print "Score average (no 0 reviews) " + str(data0.mean().item())
print "Score average (no 10 reviews) " + str(data10.mean().item())
print "Score average (no 0 or 10 reviews) " + str(data_remove_extremes.mean().item())

# check for bots
data_negative = data[(data['score'] >= 0) & (data['score'] <= 4)]
data_mixed = data[(data['score'] >= 5) & (data['score'] <= 7)]
data_positive = data[(data['score'] >= 8) & (data['score'] <= 10)]

def get_bots(sampleset):
    return sampleset[sampleset.groupby("review")["review"].transform("size") > 1]

def print_bots(id, data):
    print "Bot count[" + id + "]: " + str(data.shape[0])

def print_bots_data(id, data):
    print "Botted reviews[" + id + "]: "
    
    reviews = data["review"].unique()
    revs = {}
    for r in reviews:
        revs[r] = data[data["review"] == r]["name"].unique().tolist()
    
    for r in revs:
        print "Users " + str(revs[r]) + " - review: " + str(r)
    

bots = get_bots(data)
bots_negative = get_bots(data_negative)
bots_mixed = get_bots(data_negative)
bots_positive = get_bots(data_positive)

print_bots("all", bots)
print_bots("negative", bots_negative)
print_bots("mixed", bots_mixed)
print_bots("positive", bots_positive)

print_bots_data("all", bots)
print_bots_data("negative", bots_negative)
print_bots_data("mixed", bots_mixed)
print_bots_data("positive", bots_positive)
