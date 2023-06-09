# http://mlr.cs.umass.edu/ml/datasets/Adult
using DataFrames
using CSV
ENV["COLUMNS"] = 250;

colum_names = ["age","workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country", "mas50"]
colum_names = ["age","workclass","fnlwgt","education","educationnum","maritalstatus","occupation","relationship","race","sex","capitalgain","capitalloss","hoursperweek","nativecountry", "mas50"]
;

# df = DataFrame(CSV.File("adult.data.txt"))
# df = DataFrame(CSV.File("adult.data.txt", header = false))
# missingstrings=["NA", "na", "n/a", "missing"]

# df = DataFrame(CSV.File("adult.data.txt", 
#         header = false,
#         missingstrings=["NA", "na", "n/a", "missing", "?"],
#         delim=", "))

df = DataFrame(CSV.File("adult.data.txt", 
        header = colum_names,
        missingstring=["NA", "na", "n/a", "missing", "?"],
        delim=", "))







first(df, 5)


summary(df)

names(df)

nrow(df)

last(df)

# delete!(df,32562)
last(df)

first(df,5)

# for i in zip(names(df), eltype.(eachcol(df)))
#     println(i)
# end

#df[!,:age] = parse.(Int,df[!,:age])

# for i in zip(names(df), eltype.(eachcol(df)))
#     println(i)
# end

disallowmissing!(df, error=false);
# for i in zip(names(df), eltype.(eachcol(df)))
#     println(i)
# end

unique(df.sex)

df[(df[!,:sex] .== "male"),:sex].="Male"
df[(df[!,:sex] .== "Femle"),:sex].="Female"
df[(df[!,:sex] .== "Femle"),:sex].="Female"
df[(df[!,:sex] .== "Mal"),:sex].="Male"
df[(df[!,:sex] .== "female"),:sex].="Female"
df[(df[!,:sex] .== "Man"),:sex].="Male"

df[completecases(df),:]

using StatsBase
countmap(df[!,:workclass])

# df[(df[!,:workclass] .== missing),:workclass].="Private"
df[!,:workclass] = coalesce.(df[!,:workclass], "Private")

countmap(df[!,:workclass])

countmap(df[!,:nativecountry])

df[!,:nativecountry] = coalesce.(df[!,:nativecountry], "No country");
countmap(df[!,:nativecountry])

disallowmissing!(df, error=false);
# for i in zip(names(df), eltype.(eachcol(df)))
#     println(i)
# end

df[!,:occupation] = coalesce.(df[!,:occupation], "Not Found");
countmap(df[!,:occupation])

df = df[completecases(df),:]
disallowmissing!(df, error=false);
# for i in zip(names(df), eltype.(eachcol(df)))
#     println(i)
# end
df

# import Pkg; Pkg.add("ScikitLearn");
using ScikitLearn
using DataFrames: DataFrame, missing
@sk_import preprocessing: (LabelBinarizer, MinMaxScaler)

mapper = DataFrameMapper([
                        (:sex, LabelBinarizer()),
                        (:workclass, LabelBinarizer()),
                        ([:age], MinMaxScaler())
                        ]);

fit_transform!(mapper, copy(df))

first(df)

sort(unique(df[!,:workclass]))


