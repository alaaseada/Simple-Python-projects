from sample_madlibs import just_adjs, large_text, tell_story
import random


if __name__ == "__main__":
    m = random.choice([ just_adjs, large_text, tell_story])
    m.madlib()
