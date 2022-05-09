import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdb"]

mycol = mydb["search_result"]

# # insert

# doc = {"description":["Generations of kings were attended by these\nPokémon, which used their spectral \
#     power to\nmanipulate and control people and Pokémon.","Apparently, it can detect the innate qualities\
#         \nof leadership. According to legend, whoever it\nrecognizes is destined to become king.",\
#         "Generations of kings were attended by these\nPokémon, which used their spectral power to\
#             \nmanipulate and control people and Pokémon.","Apparently, it can detect the innate qualities\
#             \nof leadership. According to legend, whoever it\nrecognizes is destined to become king.",\
#             "In this defensive stance, Aegislash uses its steel\nbody and a force field of spectral power \
#                 to\nreduce the damage of any attack.","Its potent spectral powers allow it to manipulate\nothers. It once used its powers to force people\nand Pokémon to build a kingdom to its liking."],\
#                     "message":"Got the pokemon","name":"aegislash","status":200}

# x = mycol.insert_one(doc)

# print(x.inserted_id)

# # find
# for x in mycol.find():
#   print(x)


# # delete
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")

