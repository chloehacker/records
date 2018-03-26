# records

This is a Class object for querying a REST API.

## To install

```
git clone https://github.com/chloehacker/records.git
cd records
pip install .
```

## To use

Make sure these are installed.
```
conda install requests pandas numpy
```

```
import records
```
### The records class

```
# make a single records search
rec = records.Records("Bombus", interval=(1900, 1905))

# make a records search with additional arguments
kwargs = {"country": "CA", }
rec = records.Records("Bombus", (1900, 1905), **kwargs)

# access dataframe of results
rec.df.shape

# or a simpler view of the dataframe
rec.sdf.head()
```

```
 	species 		year 	stateProvince
0 	Bombus vagans 		1905 	Illinois
1 	Bombus centralis 	1902 	Washington
2 	Bombus vagans 		1905 	Illinois
3 	Bombus nevadensis 	1905 	Washington
4 	Bombus impatiens 	1905 	Illinois
```

### The Epochs class

```
# collect all records from 1900 to 1921 in 3 year intervals from Canada
ep = records.Epoch("Bombus", 1900, 1960, 3, **{"country": "CA"})

# show first 10 records
ep.sdf.head()

# calculate simpson's diversity (a measure of species diversity) for each state
ep.simpsons_diversity(by="stateProvince")
```

### Saving/loading data

```
# for large downloads you may want to save the dataframe to CSV.
ep.df.to_csv("data/Bombus-1900-1960-CA.csv")

# you can later reload it as an Epochs instance like the following.
ep = records.load_epochs_from_csv("data/Bombus-1900-1960-CA.csv")
```
