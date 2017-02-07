"""
Commands

Commands describe the input the player can do to the game.

"""

from evennia import Command as BaseCommand
# from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_command(): If this returns True, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_command(): Extra actions, often things done after
            every command, like prompts.

    """
    pass

#------------------------------------------------------------
#
# The default commands inherit from
#
#   evennia.commands.default.muxcommand.MuxCommand.
#
# If you want to make sweeping changes to default commands you can
# uncomment this copy of the MuxCommand parent and add
#
#   COMMAND_DEFAULT_CLASS = "commands.command.MuxCommand"
#
# to your settings file. Be warned that the default commands expect
# the functionality implemented in the parse() method, so be
# careful with what you change.
#
#------------------------------------------------------------

#from evennia.utils import utils
#class MuxCommand(Command):
#    """
#    This sets up the basis for a MUX command. The idea
#    is that most other Mux-related commands should just
#    inherit from this and don't have to implement much
#    parsing of their own unless they do something particularly
#    advanced.
#
#    Note that the class's __doc__ string (this text) is
#    used by Evennia to create the automatic help entry for
#    the command, so make sure to document consistently here.
#    """
#    def has_perm(self, srcobj):
#        """
#        This is called by the cmdhandler to determine
#        if srcobj is allowed to execute this command.
#        We just show it here for completeness - we
#        are satisfied using the default check in Command.
#        """
#        return super(MuxCommand, self).has_perm(srcobj)
#
#    def at_pre_cmd(self):
#        """
#        This hook is called before self.parse() on all commands
#        """
#        pass
#
#    def at_post_cmd(self):
#        """
#        This hook is called after the command has finished executing
#        (after self.func()).
#        """
#        pass
#
#    def parse(self):
#        """
#        This method is called by the cmdhandler once the command name
#        has been identified. It creates a new set of member variables
#        that can be later accessed from self.func() (see below)
#
#        The following variables are available for our use when entering this
#        method (from the command definition, and assigned on the fly by the
#        cmdhandler):
#           self.key - the name of this command ('look')
#           self.aliases - the aliases of this cmd ('l')
#           self.permissions - permission string for this command
#           self.help_category - overall category of command
#
#           self.caller - the object calling this command
#           self.cmdstring - the actual command name used to call this
#                            (this allows you to know which alias was used,
#                             for example)
#           self.args - the raw input; everything following self.cmdstring.
#           self.cmdset - the cmdset from which this command was picked. Not
#                         often used (useful for commands like 'help' or to
#                         list all available commands etc)
#           self.obj - the object on which this command was defined. It is often
#                         the same as self.caller.
#
#        A MUX command has the following possible syntax:
#
#          name[ with several words][/switch[/switch..]] arg1[,arg2,...] [[=|,] arg[,..]]
#
#        The 'name[ with several words]' part is already dealt with by the
#        cmdhandler at this point, and stored in self.cmdname (we don't use
#        it here). The rest of the command is stored in self.args, which can
#        start with the switch indicator /.
#
#        This parser breaks self.args into its constituents and stores them in the
#        following variables:
#          self.switches = [list of /switches (without the /)]
#          self.raw = This is the raw argument input, including switches
#          self.args = This is re-defined to be everything *except* the switches
#          self.lhs = Everything to the left of = (lhs:'left-hand side'). If
#                     no = is found, this is identical to self.args.
#          self.rhs: Everything to the right of = (rhs:'right-hand side').
#                    If no '=' is found, this is None.
#          self.lhslist - [self.lhs split into a list by comma]
#          self.rhslist - [list of self.rhs split into a list by comma]
#          self.arglist = [list of space-separated args (stripped, including '=' if it exists)]
#
#          All args and list members are stripped of excess whitespace around the
#          strings, but case is preserved.
#        """
#        raw = self.args
#        args = raw.strip()
#
#        # split out switches
#        switches = []
#        if args and len(args) > 1 and args[0] == "/":
#            # we have a switch, or a set of switches. These end with a space.
#            switches = args[1:].split(None, 1)
#            if len(switches) > 1:
#                switches, args = switches
#                switches = switches.split('/')
#            else:
#                args = ""
#                switches = switches[0].split('/')
#        arglist = [arg.strip() for arg in args.split()]
#
#        # check for arg1, arg2, ... = argA, argB, ... constructs
#        lhs, rhs = args, None
#        lhslist, rhslist = [arg.strip() for arg in args.split(',')], []
#        if args and '=' in args:
#            lhs, rhs = [arg.strip() for arg in args.split('=', 1)]
#            lhslist = [arg.strip() for arg in lhs.split(',')]
#            rhslist = [arg.strip() for arg in rhs.split(',')]
#
#        # save to object properties:
#        self.raw = raw
#        self.switches = switches
#        self.args = args.strip()
#        self.arglist = arglist
#        self.lhs = lhs
#        self.lhslist = lhslist
#        self.rhs = rhs
#        self.rhslist = rhslist
#
#        # if the class has the player_caller property set on itself, we make
#        # sure that self.caller is always the player if possible. We also create
#        # a special property "character" for the puppeted object, if any. This
#        # is convenient for commands defined on the Player only.
#        if hasattr(self, "player_caller") and self.player_caller:
#            if utils.inherits_from(self.caller, "evennia.objects.objects.DefaultObject"):
#                # caller is an Object/Character
#                self.character = self.caller
#                self.caller = self.caller.player
#            elif utils.inherits_from(self.caller, "evennia.players.players.DefaultPlayer"):
#                # caller was already a Player
#                self.character = self.caller.get_puppet(self.session)
#            else:
#                self.character = None
#

class CmdAbilities(Command):
    key = "abilities"
    aliases = ["abi"]
    lock = "cmd:all()"
    help_category = "General"
    
    def func(self):
        str, dex, con, wis, cha, int = self.caller.get_abilities()
        string = "ABILITIES \n Strength: %s \n Dexterity: %s \n Constitution: %s \n Wisdom: %s \n Charisma: %s \n Intelligence: %s \n" % (str, dex, con, wis, cha, int)
        self.caller.msg(string)
    pass

class CmdStrUp(Command):
    """
    raise the strength of a character by 1

    Usage: 
      +strengthup

    This raises the strength of the current character. This can only be 
    used during character generation.    
    """

    key = "+strengthup"
    aliases = ["+strup"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "You have no remaining points to spend on abilities."
        if not (self.caller.db.freepoints > 0):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.strength += 1
        self.caller.db.freepoints -= 1
        self.caller.msg("Your Strength is now %i. You now have %i points left to spend on abilities." % (self.caller.db.strength, self.caller.db.freepoints))

class CmdStrDown(Command):
    """
    lower the strength of a character by 1

    Usage: 
      +strengthdown

    This lowers the strength of the current character. This can only be 
    used during character generation.    
    """

    key = "+strengthdown"
    aliases = ["+strdown"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "Your Strength cannot be less than 1."
        if (self.caller.db.strength == 1):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.strength -= 1
        self.caller.db.freepoints += 1
        self.caller.msg("Your Strength is now %i. You now have %i points left to spend on abilities." % (self.caller.db.strength, self.caller.db.freepoints))

class CmdDexUp(Command):
    """
    raise the dexterity of a character by 1

    Usage: 
      +dexterityup

    This raises the dexterity of the current character. This can only be 
    used during character generation.    
    """

    key = "+dexterityup"
    aliases = ["+dexup"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "You have no remaining points to spend on abilities."
        if not (self.caller.db.freepoints > 0):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.dexterity += 1
        self.caller.db.freepoints -= 1
        self.caller.msg("Your Dexterity is now %i. You now have %i points left to spend on abilities." % (self.caller.db.dexterity, self.caller.db.freepoints))

class CmdDexDown(Command):
    """
    lower the dexterity of a character by 1

    Usage: 
      +dexteritydown

    This lowers the dexterity of the current character. This can only be 
    used during character generation.    
    """

    key = "+dexteritydown"
    aliases = ["+dexdown"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "Your Dexterity cannot be less than 1."
        if (self.caller.db.dexterity == 1):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.dexterity -= 1
        self.caller.db.freepoints += 1
        self.caller.msg("Your Dexterity is now %i. You now have %i points left to spend on abilities." % (self.caller.db.dexterity, self.caller.db.freepoints))
   
class CmdConUp(Command):
    """
    raise the constitution of a character by 1
    Usage: 
      +constitutionup
    This raises the dexterity of the current character. This can only be 
    used during character generation.    
    """
    key = "+constitutionup"
    aliases = ["+conup"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "You have no remaining points to spend on abilities."
        if not (self.caller.db.freepoints > 0):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.constitution += 1
        self.caller.db.freepoints -= 1
        self.caller.msg("Your Constitution is now %i. You now have %i points left to spend on abilities." % (self.caller.db.constitution, self.caller.db.freepoints))

class CmdConDown(Command):
    """
    lower the constitution of a character by 1

    Usage: 
      +constitutiondown

    This lowers the dexterity of the current character. This can only be 
    used during character generation.    
    """

    key = "+constitutiondown"
    aliases = ["+condown"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "Your Constitution cannot be less than 1."
        if (self.caller.db.constitution == 1):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.constitution -= 1
        self.caller.db.freepoints += 1
        self.caller.msg("Your wisstitution is now %i. You now have %i points left to spend on abilities." % (self.caller.db.wisstitution, self.caller.db.freepoints))

class CmdWisUp(Command):
    """
    raise the wisdom of a character by 1
    Usage: 
      +wisdomup
    This raises the dexterity of the current character. This can only be 
    used during character generation.    
    """
    key = "+wisdomup"
    aliases = ["+wisup"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "You have no remaining points to spend on abilities."
        if not (self.caller.db.freepoints > 0):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.wisdom += 1
        self.caller.db.freepoints -= 1
        self.caller.msg("Your Wisdom is now %i. You now have %i points left to spend on abilities." % (self.caller.db.wisdom, self.caller.db.freepoints))

class CmdWisDown(Command):
    """
    lower the wisdom of a character by 1

    Usage: 
      +wisdomdown

    This lowers the dexterity of the current character. This can only be 
    used during character generation.    
    """

    key = "+wisdomdown"
    aliases = ["+wisdown"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "Your Wisdom cannot be less than 1."
        if (self.caller.db.wisdom == 1):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.wisdom -= 1
        self.caller.db.freepoints += 1
        self.caller.msg("Your Wisdom is now %i. You now have %i points left to spend on abilities." % (self.caller.db.wisdom, self.caller.db.freepoints))

class CmdChaUp(Command):
    """
    raise the Charisma of a character by 1
    Usage: 
      +Charismaup
    This raises the dexterity of the current character. This can only be 
    used during character generation.    
    """
    key = "+charismaup"
    aliases = ["+chaup"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "You have no remaining points to spend on abilities."
        if not (self.caller.db.freepoints > 0):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.charisma += 1
        self.caller.db.freepoints -= 1
        self.caller.msg("Your Charisma is now %i. You now have %i points left to spend on abilities." % (self.caller.db.Charisma, self.caller.db.freepoints))

class CmdChaDown(Command):
    """
    lower the Charisma of a character by 1

    Usage: 
      +Charismadown

    This lowers the dexterity of the current character. This can only be 
    used during character generation.    
    """

    key = "+charismadown"
    aliases = ["+chadown"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "Your Charisma cannot be less than 1."
        if (self.caller.db.charisma == 1):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.charisma -= 1
        self.caller.db.freepoints += 1
        self.caller.msg("Your Charisma is now %i. You now have %i points left to spend on abilities." % (self.caller.db.charisma, self.caller.db.freepoints))

class CmdIntUp(Command):
    """
    raise the intelligence of a character by 1
    Usage: 
      +intelligenceup
    This raises the dexterity of the current character. This can only be 
    used during character generation.    
    """
    key = "+intelligenceup"
    aliases = ["+intup"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "You have no remaining points to spend on abilities."
        if not (self.caller.db.freepoints > 0):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.intelligence += 1
        self.caller.db.freepoints -= 1
        self.caller.msg("Your Intelligence is now %i. You now have %i points left to spend on abilities." % (self.caller.db.intelligence, self.caller.db.freepoints))

class CmdIntDown(Command):
    """
    lower the intelligence of a character by 1

    Usage: 
      +intelligencedown

    This lowers the dexterity of the current character. This can only be 
    used during character generation.    
    """

    key = "+intelligencedown"
    aliases = ["+intdown"]
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        pointerror = "Your Intelligence cannot be less than 1."
        if (self.caller.db.intelligence == 1):
            self.caller.msg(pointerror)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.intelligence -= 1
        self.caller.db.freepoints += 1
        self.caller.msg("Your Intelligence is now %i. You now have %i points left to spend on abilities." % (self.caller.db.intelligence, self.caller.db.freepoints))