import re
import logging as log


from collections import namedtuple

import sc2reader
from sc2reader.events import *
from sc2reader.objects import Participant

def get_replay_data(file):
    replays = []

    replay = sc2reader.load_replay(file, debug=True)
    players = [player for player in chain.from_iterable([team.players for team in replay.teams])
            if player.is_human
    ]

    for player in players:
        out = {}

        out['player'] = str(player)

        Event = namedtuple('Event',['frame', 'verb', 'noun', 'fullname'])

        out['events'] = []
        # Allow specification of events to `show`
        # Loop through the events
        watch_re = re.compile(r'^(Evolve|Morph|Spawn|Research|Train|Build|Upgrade)(\w+)')

        for event in player.events:
            if (isinstance(event, TargetUnitCommandEvent)
                    and event.ability_name.strip() == 'ChronoBoostEnergyCost'
            ):
                out['events'].append(Event(event.frame, 'ChronoBoost', event.target.name, f'ChronoBoost{event.target}'))
            elif (isinstance(event, CommandEvent)
                    and event.has_ability
            ):
                try:
                    match = watch_re.findall(event.ability.name)
                    if match:
                        verb = match[0][0]
                        noun = ''.join(match[0][1:])
                        out['events'].append(Event(event.frame, verb, noun, event.ability.name))
                except Exception as e:
                    log.error(f'error processing event: {event}: {e}')



        replays.append(out)

    return replays
