from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import types


class IrregularVerbs(StatesGroup):
    verbs = {                                                                                                           # Easy worlds for learning irregular verbs
        # Easy
        'hit': ('hit', 'hit', 'hit', "Ударять", "ударять", "поражать", "Поражать"), 'cut': ('cut', 'cut', 'cut'),
        'let': ('let', 'let', 'let'), 'put': ('put', 'put', 'put'), 'set': ('set', 'set', 'set'),
        'read': ('read', 'read'  'read'), 'shut': ('shut ', 'shut', 'shut'), 'bet': ('bet', 'bet', 'bet'),
        'broadcast': ('broadcast', 'broadcast', 'broadcast'), 'burst': ('burst', 'burst', 'burst'),
        # Middle
        'cost': ('cost', 'cast', 'cost'),
        'build': ('build', 'built', 'built'),
        'say': ('say', 'said', 'said'),
        'breed': ('breed', 'bred', 'bred'),
        'find': ('find', 'found', 'found'),
        'tell': ('tell', 'told', 'told'),
        'bend': ('bend', 'bent', 'bent'),
        'lead': ('lead', 'led', 'led'),
        'bleed': ('bleed', 'bled', 'bled'),
        'burn': ('burn', 'burnt', 'burnt', 'burned'),
        '': (),
        # Ending (ought)
        'bring': ('bring', 'brought', 'brought'), 'buy': ('buy', 'bought', 'bought'),
        'catch': ('catch', 'caught', 'caught'), 'fight': ('fight', 'fought', 'fought'),
        'seek': ('seek', 'sought', 'sought'), 'teach': ('teach', 'taught', 'taught'),
        'think': ('think', 'thought', 'thought'),
        # Ending (en)
        'awake': ('awake', 'awoke', 'awoken'), 'arise': ('arise', 'arose', 'arisen'),
        'beat': ('beat', 'beat', 'beaten'), 'bite': ('bite', 'bit', 'bitten'), 'break': ('break', 'broke', 'broken'),
        'choose': ('choose', 'chose', 'chosen'), 'drive': ('drive', 'drove', 'driven'),
        'eat': ('eat', 'ate', 'eaten'), 'fall': ('fall', 'fell', 'fallen'),
        'forget': ('forget', 'forgot', 'forgotten'), 'forgive': ('forgive', 'forgave', 'forgiven'),
        'freeze': ('freeze', 'froze', 'frozen'),
        'give': ('give', 'gave', 'given'), 'hide': ('hide', 'hid', 'hidden'),
        'ride': ('ride', 'rode', 'ridden'), 'rise': ('rise', 'rose', 'risen'),
        'see': ('see', 'saw', 'seen'), 'shake': ('shake', 'shook', 'shaken'),
        'speak': ('speak', 'spoke', 'spoken'), 'steal': ('steal', 'stole', 'stolen'),
        'wake': ('wake', 'woke', 'woken'), 'write': ('write', 'wrote', 'written'),
        'get': ('get', 'got', 'gotten'), 'forbid': ('forbid', 'forbade', 'forbidden'),
        'overtake': ('overtake', 'overtook', 'overtaken'), 'swell': ('swell', 'swelled', 'swollen', 'swelled')
    }
