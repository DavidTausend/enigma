from enigma.machine import EnigmaMachine
from enig.util import clear_screen


def setup_enigma_machine(ring_settings):
    """
    Setting up Enigma machine with predefined settings.
    """
    clear_screen()

    machine = EnigmaMachine.from_key_sheet(
        rotors='II IV V',
        reflector='B',
        ring_settings=ring_settings,
        plugboard_settings='AD FG'
    )
    return machine


def encrypt_string(machine, plaintext, initial_positions):
    """
    Encrypts a string using the Enigma machine.
    """
    machine.set_display(initial_positions)
    ciphertext = machine.process_text(plaintext)
    return ciphertext, initial_positions
