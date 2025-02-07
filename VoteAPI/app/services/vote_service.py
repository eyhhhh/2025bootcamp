VOTE_KEY = "vote"
MEMBERS = ["Trump", "Biden", "Obama"]

class VoteService:
  def members(self)->list[str]:
    return MEMBERS
  
  async def vote(self, redis, member_id:int)->bool:
    try:
    # ZINCRBY(key, increment, member)
      await redis.zincrby(VOTE_KEY, 1, MEMBERS[member_id]) #예외처리는 라우터에서
    except TypeError as e:
      print(e)
      return False
    return True
  
  async def score(self, redis):
    # ZRANGE(key,start,stop,[WITHSCORES],[REV]):
    scores = await redis.zrevrange(VOTE_KEY, 0, -1)
    return scores