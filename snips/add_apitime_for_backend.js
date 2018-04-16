db.eventV4.ensureIndex({
    "serverTime": 1,
    "apiTime": 1
});
print("Index building ...")


var totalDocs = db.eventV4.count({})
print("Total Size: " + totalDocs)


var processQueueDocsNum = db.eventV4.count({
    "serverTime": {"$exists": true},
    "apiTime": {"$exists": false}
})
print("Total Process Size: " + processQueueDocsNum)


var nowNum = 1
db.eventV4.find({
    "serverTime": {"$exists": true},
    "apiTime": {"$exists": false}
}).forEach(function (doc) {
    db.eventV4.update(
        { "_id": doc._id },
        { "$set": {"apiTime": doc.serverTime.getTime()} }
    )
    print("Processing "+ nowNum++ +"/" + processQueueDocsNum + " < " + totalDocs)
});

/**
$ mongo backend10 ./addApiTimeForBackendEvents.js
MongoDB shell version: 3.2.8
connecting to: backend10
Background index building ...
Total Process Size: 3
Total Size: 10
Processing 1/3 < 10
Processing 2/3 < 10
Processing 3/3 < 10
**/
