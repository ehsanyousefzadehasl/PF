numOfVotes=int(input());

votesDictionary = dict();

for i in range(0, numOfVotes):
	inVote = input();
	if inVote in votesDictionary:
		votesDictionary[inVote] += 1;
	else:
		votesDictionary[inVote] = 1;

ourList = sorted(list(votesDictionary.keys()))
for this_one in ourList:
	print('%s %s' % (this_one, votesDictionary[this_one]))