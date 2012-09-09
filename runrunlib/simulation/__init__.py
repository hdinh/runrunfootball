from .pregame import pipeline as pregame_pipeline
from .ingame import pipeline as ingame_pipeline
from .postgame import pipeline as postgame_pipeline

pipeline = (pregame_pipeline,
            ingame_pipeline,
            postgame_pipeline)
