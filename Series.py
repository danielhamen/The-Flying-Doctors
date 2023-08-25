class Episode:
    def __init__(self, name: str, index: int, url: str):
        self.name = name
        self.index = index
        self.url = url


index = {
    "1": {
        "1": Episode("Will to Survive", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=1"),
        "2": Episode("Trial By Gossip", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=2"),
        "3": Episode("Hot Enough For You ", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=3"),
        "4": Episode("Dreams of Sand ", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=4"),
        "5": Episode("Public Property", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=5"),
        "6": Episode("Is Nothing Sacred  ", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=6"),
        "7": Episode("Square Pegs    ", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=7"),
        "8": Episode("Sins of the Fathers", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=8"),
        "9": Episode("Rally to the Cause ", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=9"),
        "10": Episode("Talk of the Town   ", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=10"),
        "11": Episode("Do You Read Me ", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=11"),
        "12": Episode("E.T. - New Girl in Town", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=12"),
        "13": Episode("A Choice of Enemies", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=13"),
        "14": Episode("Departures", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=14"),
        "15": Episode("A Lost Generation", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=15"),
        "16": Episode("Someone Special", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=16"),
        "17": Episode("Return of the Hero", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=17"),
        "18": Episode("Eye of the Beholder", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=18"),
        "19": Episode("Million-acre Prison", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=19"),
        "20": Episode("Like a Death in the Family", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=20"),
        "21": Episode("Fearless Frank", 21, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=21"),
        "22": Episode("Forgiveness", 22, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=22"),
        "23": Episode("Acceptance", 23, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=23"),
        "24": Episode("The Show Goes On", 24, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=24"),
        "25": Episode("To The Rescue (1)", 25, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=25"),
        "26": Episode("Into The Future (2", 26, "https://multiembed.mov/?video_id=4014&tmdb=1&s=1&e=26"),
    }, "2": {
        "1": Episode("Good Day For It", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=1"),
        "2": Episode("Horses For Courses", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=2"),
        "3": Episode("The Unluckiest Boy in Town", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=3"),
        "4": Episode("It Isn't Cricket", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=4"),
        "5": Episode("An Only Child", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=5"),
        "6": Episode("A Love Story", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=6"),
        "7": Episode("Keeping Up Appearances", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=7"),
        "8": Episode("All Things Bright and Beautiful", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=8"),
        "9": Episode("My Name is Sky", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=9"),
        "10": Episode("Bachelors & Spinsters", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=10"),
        "11": Episode("Fifty-two Hours Straight", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=11"),
        "12": Episode("A Friend of a Friend", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=12"),
        "13": Episode("Friends and Lovers", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=13"),
        "14": Episode("Realms of Gold", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=14"),
        "15": Episode("The Hometown Hero", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=15"),
        "16": Episode("A Distant Echo", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=16"),
        "17": Episode("No Laughing Matter", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=17"),
        "18": Episode("No Quarter Asked", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=18"),
        "19": Episode("Myths & Legends", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=19"),
        "20": Episode("The Hitch-hiker", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=20"),
        "21": Episode("Give a Dog a Bad Name", 21, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=21"),
        "22": Episode("Everyday a Gift", 22, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=22"),
        "23": Episode("Bearing Gifts", 23, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=23"),
        "24": Episode("Repeat Performance", 24, "https://multiembed.mov/?video_id=4014&tmdb=1&s=2&e=24")
    }, "3": {
        "1": Episode("The Noble Art", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=1"),
        "2": Episode("Sapphire", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=2"),
        "3": Episode("Cries From The Heart", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=3"),
        "4": Episode("All In A Day's Work", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=4"),
        "5": Episode("Out Of A Clear Blue Sky", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=5"),
        "6": Episode("Affirmative Action", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=6"),
        "7": Episode("Figures In A Landscape", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=7"),
        "8": Episode("The Devil You Know", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=8"),
        "9": Episode("Operation Solo", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=9"),
        "10": Episode("The Path Of True Love", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=10"),
        "11": Episode("The Kid", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=11"),
        "12": Episode("The First Step", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=12"),
        "13": Episode("Hopscotch", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=13"),
        "14": Episode("Jacks High", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=14"),
        "15": Episode("Clapped Out", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=15"),
        "16": Episode("Private Lives, Public Faces", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=16"),
        "17": Episode("Wedlock", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=17"),
        "18": Episode("The Wrangler's Daughter", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=18"),
        "19": Episode("Borrowed Time", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=19"),
        "20": Episode("The Forbidden", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=20"),
        "21": Episode("She'll Be Right", 21, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=21"),
        "22": Episode("One Final Request", 22, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=22"),
        "23": Episode("Roxanne", 23, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=23"),
        "24": Episode("Don't Tell Anybody", 24, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=24"),
        "25": Episode("No Way Back", 25, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=25"),
        "26": Episode("Johnnie Come Home", 26, "https://multiembed.mov/?video_id=4014&tmdb=1&s=3&e=26")
    }, "4": {
        "1": Episode("Look, Up In The Sky", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=1"),
        "2": Episode("Preacher Man", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=2"),
        "3": Episode("The Fear (Part 1)", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=3"),
        "4": Episode("The Fear (Part 2)", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=4"),
        "5": Episode("Fair Go", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=5"),
        "6": Episode("Broken Airwaves", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=6"),
        "7": Episode("Bed And Board", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=7"),
        "8": Episode("Breaking The Drought", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=8"),
        "9": Episode("Family Secrets (Part 1)", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=9"),
        "10": Episode("Family Secrets (Part 2)", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=10"),
        "11": Episode("All You Need Is Luck", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=11"),
        "12": Episode("The Silly Season", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=12"),
        "13": Episode("Every Situation", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=13"),
        "14": Episode("The Storyteller", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=14"),
        "15": Episode("The Choice", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=15"),
        "16": Episode("A Shade Of Doubt", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=16"),
        "17": Episode("Mick & Julia", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=17"),
        "18": Episode("The Deal", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=18"),
        "19": Episode("A Thing Of Beauty", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=19"),
        "20": Episode("Cadenza", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=20"),
        "21": Episode("Mates", 21, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=21"),
        "22": Episode("The Child", 22, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=22"),
        "23": Episode("Next To Go", 23, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=23"),
        "24": Episode("Gotta Have Friends", 24, "https://multiembed.mov/?video_id=4014&tmdb=1&s=4&e=24")
    }, "5": {
        "1": Episode("The Gift", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=1"),
        "2": Episode("Second Chance", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=2"),
        "3": Episode("Not The Malarvys", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=3"),
        "4": Episode("The Adventure", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=4"),
        "5": Episode("No Man's Land", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=5"),
        "6": Episode("Rising Sundown", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=6"),
        "7": Episode("Man And Boy", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=7"),
        "8": Episode("The Longing", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=8"),
        "9": Episode("Bitter Harvest", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=9"),
        "10": Episode("The Instrument", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=10"),
        "11": Episode("Word & Deed", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=11"),
        "12": Episode("All That Glitters", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=12"),
        "13": Episode("Fly Past", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=13"),
        "14": Episode("The Last Rodeo", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=14"),
        "15": Episode("Sky Above, Earth Below", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=15"),
        "16": Episode("Lucky Lady", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=16"),
        "17": Episode("The Chips Are Down", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=17"),
        "18": Episode("Guardian Angel", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=18"),
        "19": Episode("Battlers", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=19"),
        "20": Episode("No Tears", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=20"),
        "21": Episode("A Doctor's Dreaming", 21, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=21"),
        "22": Episode("Blues For Judy", 22, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=22"),
        "23": Episode("The Claim", 23, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=23"),
        "24": Episode("A Rhyme For Reason", 24, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=24"),
        "25": Episode("Dad's Little Bloke", 25, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=25"),
        "26": Episode("A Sporting Life", 26, "https://multiembed.mov/?video_id=4014&tmdb=1&s=5&e=26")
    }, "6": {
        "1": Episode("A Good Drop Of Red", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=1"),
        "2": Episode("The Hero", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=2"),
        "3": Episode("Suspicion", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=3"),
        "4": Episode("Daddy's Girl", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=4"),
        "5": Episode("Two Sisters Running", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=5"),
        "6": Episode("Dangerous Games", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=6"),
        "7": Episode("Milk Run", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=7"),
        "8": Episode("Point Of No Return", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=8"),
        "9": Episode("Small Mercies", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=9"),
        "10": Episode("A Painful Extraction", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=10"),
        "11": Episode("The Climber", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=11"),
        "12": Episode("Dead Reckoning", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=12"),
        "13": Episode("A Bride to Be", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=13"),
        "14": Episode("A Place For The Night", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=14"),
        "15": Episode("End Of The Rainbow", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=15"),
        "16": Episode("Double Vision", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=16"),
        "17": Episode("The Boy In The Boot", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=17"),
        "18": Episode("Windows Of The Soul", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=18"),
        "19": Episode("Rest In Peace", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=19"),
        "20": Episode("Life Line", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=6&e=20")
    },
    "7": {
        "1": Episode("Fly Like A Bird", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=1"),
        "2": Episode("A Day To Remember", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=2"),
        "3": Episode("A Place To Call Home", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=3"),
        "4": Episode("Divided Loyalties", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=4"),
        "5": Episode("A Rural Education", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=5"),
        "6": Episode("The Ties That Bind", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=6"),
        "7": Episode("Brother’s Keeper", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=7"),
        "8": Episode("Wilderness", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=8"),
        "9": Episode("Valentine’s Day", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=9"),
        "10": Episode("A Little Tenderness", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=10"),
        "11": Episode("Poet’s Corner", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=11"),
        "12": Episode("Family Farm", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=12"),
        "13": Episode("A Place Where You Belong", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=13"),
        "14": Episode("Break Away", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=14"),
        "15": Episode("Billie and Pete", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=15"),
        "16": Episode("Old Man Weed", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=16"),
        "17": Episode("David and Goliath", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=17"),
        "18": Episode("Last Carnival", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=18"),
        "19": Episode("Innocence Lost", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=19"),
        "20": Episode("Bush Christmas", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=7&e=20")
    },
    "8": {
        "1": Episode("What A Guy", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=1"),
        "2": Episode("Bad Moon Rising", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=2"),
        "3": Episode("A New Life", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=3"),
        "4": Episode("Through Thick And Thin", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=4"),
        "5": Episode("Deceptions", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=5"),
        "6": Episode("None So Blind", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=6"),
        "7": Episode("Sleep Of Reason", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=7"),
        "8": Episode("My Mother’s Child", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=8"),
        "9": Episode("Swinging On The Rope", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=9"),
        "10": Episode("Father and Son", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=10"),
        "11": Episode("A Little Miracle", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=11"),
        "12": Episode("Murphy’s Law", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=12"),
        "13": Episode("Breaking down the wall", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=13"),
        "14": Episode("Once Bitten", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=14"),
        "15": Episode("Clipped Wings", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=15"),
        "16": Episode("Walk Don’t Run", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=16"),
        "17": Episode("Masquerade", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=17"),
        "18": Episode("Against The Current", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=18"),
        "19": Episode("Last Of The Cochranes", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=19"),
        "20": Episode("Double Life", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=20"),
        "21": Episode("Something, Nothing", 21, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=21"),
        "22": Episode("Family", 22, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=22"),
        "23": Episode("Being Positive", 23, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=23"),
        "24": Episode("Open Day", 24, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=24"),
        "25": Episode("Changing Times", 25, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=25"),
        "26": Episode("Freedom", 26, "https://multiembed.mov/?video_id=4014&tmdb=1&s=8&e=26")
    },
    "9": {
        "1": Episode("Nymphs and Nightmares", 1, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=1"),
        "2": Episode("Out Of The Blue", 2, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=2"),
        "3": Episode("The Last Dance", 3, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=3"),
        "4": Episode("Unfinished Business", 4, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=4"),
        "5": Episode("Jacqueline", 5, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=5"),
        "6": Episode("Monkey", 6, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=6"),
        "7": Episode("The Stranger", 7, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=7"),
        "8": Episode("The Christening", 8, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=8"),
        "9": Episode("The Good Book", 9, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=9"),
        "10": Episode("My Little Patch", 10, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=10"),
        "11": Episode("Two Splatt Shuffle", 11, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=11"),
        "12": Episode("Secrets", 12, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=12"),
        "13": Episode("The Games We Play", 13, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=13"),
        "14": Episode("Bone China", 14, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=14"),
        "15": Episode("Johnno Be Good", 15, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=15"),
        "16": Episode("Lost Rainbows", 16, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=16"),
        "17": Episode("Broken Promises", 17, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=17"),
        "18": Episode("Visitors Welcome", 18, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=18"),
        "19": Episode("Yesterday’s News", 19, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=19"),
        "20": Episode("Dirty Linen", 20, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=20"),
        "21": Episode("Chasing Rainbows", 21, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=21"),
        "22": Episode("Uncle Cyrano", 22, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=22"),
        "23": Episode("Luck Of The Draw", 23, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=23"),
        "24": Episode("Trouble with M.E.", 24, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=24"),
        "25": Episode("The Accomplice", 25, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=25"),
        "26": Episode("Blind Obsession", 26, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=26"),
        "27": Episode("Wimp", 27, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=27"),
        "28": Episode("Visionaries", 28, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=28"),
        "29": Episode("Life Lessons", 29, "https://multiembed.mov/?video_id=4014&tmdb=1&s=9&e=29")
    },
}

import os

def get_episode():
    os.system("cls")
    seasons = "\n  ".join([f"({x}): Season {x}" for x in range(1, 10)])
    s = input(f"""Which season would you like to watch?:
  {seasons}

>>> (1 - 9): """)
    if s.lower() == "q":
        exit("Exited.")

    try:
      if 1 > int(s) > 9:
          print("Error: Invalid season")
      else:
        episodes = index[s]

        print(f"Found {len(episodes)} episodes! Select one:")
        aep = episodes

        episodes = [ep for ind,ep in episodes.items()]
        episodes = [f"""({x.index}){'' if x.index > 9 else ' '} {x.name}""" for x in episodes]
        l = len(episodes)
        episodes = "\n  ".join(episodes)
        e = input(f"""  {episodes}

  >>> (1 - {l}): """)
        if e.lower() == "q":
           exit("Exited.")

        input(f"\nPress enter to open Season {s}, Episode {e}: {aep[e].name}...")
        os.system(f"start chrome.exe \"{aep[e].url}\"")

    except:
       print("Error: Invalid season")

    c = input("Session ended. Would you like to start again (y/N)? ")
    if c.lower() in ["y", ""]:
       get_episode()
    else:
       exit("Exited.")

while True:
    x = input("Created by Daniel Hamen\n\nPress enter to start (at any time, input 'Q' to exit)...")
    if x.lower() == "q":
       exit("Exited.")

    get_episode()