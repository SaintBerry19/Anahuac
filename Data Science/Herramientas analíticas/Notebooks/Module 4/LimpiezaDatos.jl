# https://archive.ics.uci.edu/ml/datasets/adult (Anteriormente http://mlr.cs.umass.edu/ml/datasets/Adult)
using DataFrames
using CSV
ENV["COLUMNS"] = 250;

column_names = ["age","workclass","fnlwgt","education","educationnum","maritalstatus","occupation","relationship","race","sex","capitalgain","capitalloss","hoursperweek","nativecountry", "mas50"]
;

df = DataFrame(CSV.File("C:\\Users\\User\\Desktop\\No games\\Diplomado\\Anahuac\\Data Science\\Herramientas analíticas\\Notebooks\\Material 1_7_2\\adult.data.txt", 
        header = column_names,
        missingstring=["NA", "na", "n/a", "missing", "?"],
        delim=", "))
nrow(df)
last(df)

delete!(df,32561)
nrow(df)


last(df)

names(df)

summary(df)

first(df,5)

for i in zip(names(df), eltype.(eachcol(df)))
    println(i)
end

disallowmissing!(df, error=false);
for i in zip(names(df), eltype.(eachcol(df)))
    println(i)
end

df[!,:age] = convert.(Int,df[!,:age])

unique(df.sex)

df[(df[!,:sex] .== "male"),:sex].="Male"
df[(df[!,:sex] .== "Femle"),:sex].="Female"
df[(df[!,:sex] .== "Femle"),:sex].="Female"
df[(df[!,:sex] .== "Mal"),:sex].="Male"
df[(df[!,:sex] .== "female"),:sex].="Female"
df[(df[!,:sex] .== "Man"),:sex].="Male"

unique(df.sex)

df[completecases(df),:]

using Pkg
Pkg.add("StatsBase")
using StatsBase
countmap(df[!,:workclass])

# df[(df[!,:workclass] .== missing),:workclass].="Private" No funciona porque aqui no hay nulos
df[!,:workclass] = coalesce.(df[!,:workclass], "Private")

countmap(df[!,:workclass])

countmap(df[!,:"nativecountry"])[missing]

df[!,:"native-country"] = coalesce.(df[!,:"nativecountry"], "No country");
countmap(df[!,:"nativecountry"])

disallowmissing!(df, error=false);
for i in zip(names(df), eltype.(eachcol(df)))
    println(i)
end

df[!,:occupation] = coalesce.(df[!,:occupation], "Not Found");
countmap(df[!,:occupation])

df = df[completecases(df),:]
disallowmissing!(df, error=false);
for i in zip(names(df), eltype.(eachcol(df)))
    println(i)
end
df

Pkg.add("ScikitLearn")
using ScikitLearn
using DataFrames: DataFrame, missing
@sk_import preprocessing: (LabelBinarizer, MinMaxScaler)

Pkg.update()

mapper = DataFrameMapper([
                        (:sex, LabelBinarizer()),
                        (:workclass, LabelBinarizer()),
                        ([:age], MinMaxScaler())
                        ]);

fit_transform!(mapper, copy(df))

first(df)

sort(unique(df[!,:workclass]))


