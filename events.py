import utilities
import monsters

events = ['''Sky Whale: A sky whale can be seen playing in the clouds,
it disappears after 1d8 hours''',
'''Faerie dragon puzzle (details in notes)''',
'''Wolf Howl: A Druid has died. His animal companion was a wolf.
A lone howl in the night always comes from the east.
Every night the group hears the howls.
If they follow the sounds it leads to a Druid Cave and his grim remains''',
'''A noble wanting to be brought home (reward 500 gp)''',
'(New/old) remains of {} killed by {}'.format(monsters.mobRandomTrue().name, monsters.mobRandomTrue().name),
'An injured {}'.format(monsters.mobRandomTrue().name)]
