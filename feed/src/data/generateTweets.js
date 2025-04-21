const fs = require('fs');
const path = require('path');

const getRandomInt = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};

const getRandomDate = () => {
  const now = new Date();
  const pastYear = new Date(now.getFullYear() - 1, now.getMonth(), now.getDate());
  const randomTime = pastYear.getTime() + Math.random() * (now.getTime() - pastYear.getTime());
  return new Date(randomTime);
};

const generateUserData = (count) => {
  const firstNames = ['John', 'Jane', 'Michael', 'Emma', 'David', 'Sarah', 'James', 'Emily', 'Robert', 'Olivia', 
                     'William', 'Sophia', 'Joseph', 'Ava', 'Thomas', 'Isabella', 'Charles', 'Mia', 'Daniel', 'Charlotte'];
  const lastNames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
                    'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson'];
  
  const users = [];
  
  for (let i = 0; i < count; i++) {
    const firstName = firstNames[getRandomInt(0, firstNames.length - 1)];
    const lastName = lastNames[getRandomInt(0, lastNames.length - 1)];
    const displayName = `${firstName} ${lastName}`;
    const username = (firstName + lastName + getRandomInt(1, 999)).toLowerCase();
    
    users.push({
      id: `user_${i + 1}`,
      username,
      displayName
    });
  }
  
  return users;
};

const tweetContents = [
  "Just had the most amazing coffee at that new place downtown!",
  "Can't believe it's already the weekend! Time flies.",
  "New personal best at the gym today. Feeling strong!",
  "This weather is perfect for a beach day.",
  "Just finished reading an amazing book. Highly recommend!",
  "Traffic was terrible this morning. Late for work again.",
  "So excited for the concert tonight!",
  "Just adopted the cutest puppy from the shelter.",
  "My flight got delayed. Stuck at the airport for hours.",
  "Made the most delicious homemade pasta for dinner tonight.",
  "The new update on my phone is driving me crazy.",
  "Just watched the season finale. Mind blown!",
  "Anyone else having internet problems today?",
  "Hiking in the mountains today. The view is breathtaking!",
  "Happy birthday to my best friend! Love you lots.",
  "Pulled an all-nighter to finish this project. Need coffee now.",
  "Feeling grateful for all the support from my friends.",
  "Just got tickets to see my favorite band next month!",
  "Starting a new job tomorrow. Excited and nervous!",
  "My garden is blooming beautifully this spring.",
  "Trying out that new recipe I found online.",
  "Can anyone recommend a good movie to watch tonight?",
  "Missing summer days already as fall begins.",
  "Working from home has its perks. No commute!",
  "Just witnessed the most beautiful sunset.",
  "Technology these days is advancing so quickly!",
  "Finding it hard to stay motivated today.",
  "Celebrating my promotion today! Hard work pays off.",
  "The customer service at this place is horrible.",
  "Who else is watching the game tonight?",
  "Just got back from an amazing vacation.",
  "Struggling with these tough decisions lately.",
  "My kids said the funniest thing today. Still laughing!",
  "Looking forward to the long weekend.",
  "The new restaurant in town is definitely worth trying.",
  "Feeling inspired after attending that workshop.",
  "Nothing beats a quiet evening with a good book.",
  "Lost my keys again. Third time this week!",
  "Reconnected with an old friend today. So nice to catch up!",
  "The new policy at work makes no sense at all.",
  "Just donated to my favorite charity. Feels good to help.",
  "Trying to learn a new language is harder than I thought.",
  "The art exhibition downtown is incredible!",
  "Weekend plans cancelled due to rain. Staying in it is!",
  "Anyone else feel like this week is dragging on forever?",
  "Just ran my first marathon! Exhausted but proud.",
  "Home repairs are costing more than expected.",
  "Made some amazing new friends at the event last night.",
  "The customer service at this hotel exceeded my expectations!",
  "The price of groceries these days is outrageous."
];

const generateTweet = (id, user, timestamp) => {
  const content = tweetContents[getRandomInt(0, tweetContents.length - 1)];
  const likes = getRandomInt(0, 5000);
  const retweets = getRandomInt(0, Math.floor(likes * 0.7));
  const replies = getRandomInt(0, Math.floor(likes * 0.3));
  
  return {
    id,
    username: user.username,
    displayName: user.displayName,
    content,
    timestamp: timestamp.toISOString(),
    likes,
    retweets,
    replies
  };
};

const generateTweetDataset = (tweetCount = 100000) => {
  const userCount = Math.max(Math.floor(tweetCount / 10), 1000); 
  const users = generateUserData(userCount);
  const tweets = [];
  
  for (let i = 0; i < tweetCount; i++) {
    const user = users[getRandomInt(0, users.length - 1)];
    const timestamp = getRandomDate();
    const tweet = generateTweet(`tweet_${i + 1}`, user, timestamp);
    tweets.push(tweet);
  }

  tweets.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
  
  return {
    users,
    tweets
  };
};

const dataset = generateTweetDataset(100000);
const outputDir = path.join(__dirname);

fs.writeFileSync(
  path.join(outputDir, 'tweets.json'),
  JSON.stringify(dataset.tweets, null, 2)
);

console.log(`Generated ${dataset.tweets.length} tweets from ${dataset.users.length} users`);
console.log(`Data saved to ${outputDir}/tweets.json`); 