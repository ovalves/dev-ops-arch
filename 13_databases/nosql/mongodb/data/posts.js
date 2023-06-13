db = db.getSiblingDB("newsfeed");

db.createCollection('posts', { capped: false });

db['posts'].insertMany([
    {
        user_id: "123456",
        content: "Olá mundo",
        likes: 3,
        comments: 5,
        shared: 1,
        created_at: new Date("2023-03-23T20:20:00.868+00:00")
    }
])
