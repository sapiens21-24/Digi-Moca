# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import time
import os
import boto3
from datetime import datetime
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_dynamodb.adapter import DynamoDbAdapter
# initialize persistence adapter
ddb_region = os.environ.get('DYNAMODB_PERSISTENCE_REGION')
ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')

ddb_resource = boto3.resource('dynamodb', region_name=ddb_region)
dynamodb_adapter = DynamoDbAdapter(table_name=ddb_table_name, create_table=False, dynamodb_resource=ddb_resource)

from ask_sdk_model import Response

from state import *
from f_words import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")
        attr = handler_input.attributes_manager.persistent_attributes
        if not attr: # Init attr
            attr['test_state'] = vars(State())
            attr['test_state']['item'] = MEMORY
            attr['test_state']['step'] = 1
            attr['test_state']['date'] = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        else:
            item = int(attr['test_state']['item'])
            step = int(attr['test_state']['step'])
            attr['test_state']['item'] = item
            attr['test_state']['step'] = step
            attr['test_state']['forward_numbers'] = int(attr['test_state']['forward_numbers'])
            attr['test_state']['backward_numbers'] = int(attr['test_state']['backward_numbers'])
            attr['test_state']['score'] = int(attr['test_state']['score'])
            attr['test_state']['letter_mistakes'] = int(attr['test_state']['letter_mistakes'])
            attr['test_state']['first_sentence'] = int(attr['test_state']['first_sentence'])
            attr['test_state']['second_sentence'] = int(attr['test_state']['second_sentence'])
            attr['test_state']['transport'] = int(attr['test_state']['transport'])
            attr['test_state']['measure'] = int(attr['test_state']['measure'])
            attr['test_state']['day'] = int(attr['test_state']['day'])
            attr['test_state']['year'] = int(attr['test_state']['year'])
            attr['test_state']['afaga'] = int(attr['test_state']['afaga'])
            attr['test_state']['vigo'] = int(attr['test_state']['vigo'])
            if item == ATTENTION and step == 36: attr['test_state']['calculations'] = [] #step == 16
            #if item == LANGUAGE and step == 6: attr['test_state']['f_words'] = []

        handler_input.attributes_manager.session_attributes = attr
        handler_input.attributes_manager.save_persistent_attributes()

        item = list(TEST)[attr['test_state']['item']]
        step = attr['test_state']['step']
        attr['test_state']['letters_last_time'] = str(time.time())
        #attr['test_state']['f_start_time'] = str(time.time())
        return handler_input.response_builder.speak(TEST[item][step-1]["speak"]).ask(TEST[item][step-1]["reprompt"]).response


class RememberIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("RememberIntent")(handler_input) and full_state in ['12', '13', '51', '52', '53', '54', '55', '56', '57', '58', '59', '510', '511'])
        
    def handle(self, handler_input):
        logger.info("In RememberIntentHandler")
        state = handler_input.attributes_manager.session_attributes['test_state']

        if state['item'] == DELAYED_RECALL:
            if state['step'] == 1:
                recuerdos = handler_input.request_envelope.request.intent.slots
                for recuerdo in recuerdos:
                    if recuerdos[recuerdo].value not in state['unclued_recalls']:
                        state['unclued_recalls'] += [recuerdos[recuerdo].value]

                if "rostro" not in state['unclued_recalls']:
                    state['step']= 1 # I know, we already in it...
                elif "seda" not in state['unclued_recalls']:
                    state['step'] = 3
                elif "templo" not in state['unclued_recalls']:
                    state['step'] = 5
                elif "clavel" not in state['unclued_recalls']:
                    state['step'] = 7
                elif "rojo" not in state['unclued_recalls']:
                    state['step'] = 9
                else: # We have em all
                    state['step'] = 11
                
            elif state['step'] == 2:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "rostro":
                    state['clued_recalls'] += ['rostro']
                    if "seda" not in state['unclued_recalls']:
                        state['step'] = 3
                    elif "templo" not in state['unclued_recalls']:
                        state['step'] = 5
                    elif "clavel" not in state['unclued_recalls']:
                        state['step'] = 7
                    elif "rojo" not in state['unclued_recalls']:
                        state['step'] = 9
                    else: # We have em all
                        state['step'] = 11
                
            elif state['step'] == 3:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "rostro":
                    state['choice_recalls'] += ['rostro']
                    
                if "seda" not in state['unclued_recalls']:
                    state['step'] = 3
                elif "templo" not in state['unclued_recalls']:
                    state['step'] = 5
                elif "clavel" not in state['unclued_recalls']:
                    state['step'] = 7
                elif "rojo" not in state['unclued_recalls']:
                    state['step'] = 9
                else: # We have em all
                    state['step'] = 11
                
            elif state['step'] == 4:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "seda":
                    state['clued_recalls'] += ['seda']
                    if "templo" not in state['unclued_recalls']:
                        state['step'] = 5
                    elif "clavel" not in state['unclued_recalls']:
                        state['step'] = 7
                    elif "rojo" not in state['unclued_recalls']:
                        state['step'] = 9
                    else: # We have em all
                        state['step'] = 11
                
            elif state['step'] == 5:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "seda":
                    state['choice_recalls'] += ['seda']
                    
                if "templo" not in state['unclued_recalls']:
                    state['step'] = 5
                elif "clavel" not in state['unclued_recalls']:
                    state['step'] = 7
                elif "rojo" not in state['unclued_recalls']:
                    state['step'] = 9
                else: # We have em all
                    state['step'] = 11
                
            elif state['step'] == 6:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "templo":
                    state['clued_recalls'] += ['templo']
                    if "clavel" not in state['unclued_recalls']:
                        state['step'] = 7
                    elif "rojo" not in state['unclued_recalls']:
                        state['step'] = 9
                    else: # We have em all
                        state['step'] = 11
                
            elif state['step'] == 7:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "templo":
                    state['choice_recalls'] += ['templo']
                    
                if "clavel" not in state['unclued_recalls']:
                    state['step'] = 7
                elif "rojo" not in state['unclued_recalls']:
                    state['step'] = 9
                else: # We have em all
                    state['step'] = 11
                
            elif state['step'] == 8:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "clavel":
                    state['clued_recalls'] += ['clavel']
                    if "rojo" not in state['unclued_recalls']:
                        state['step'] = 9
                    else: # We have em all
                        state['step'] = 11
                
            elif state['step'] == 9:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "clavel":
                    state['choice_recalls'] += ['clavel']
                    
                if "rojo" not in state['unclued_recalls']:
                    state['step'] = 9
                else: # We have em all
                    state['step'] = 11
                
            elif state['step'] == 10:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "rojo":
                    state['clued_recalls'] += ['rojo']
                    state['step'] = 11
                
            elif state['step'] == 11:
                if handler_input.request_envelope.request.intent.slots['recuerdo_uno'].value == "rojo":
                    state['choice_recalls'] += ['rojo']
                
        return NextIntentHandler().handle(handler_input)


class YesIntentHandler(AbstractRequestHandler):
    """Handler for Yes Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("AMAZON.YesIntent")(handler_input))# and full_state in ['11', '21', '23', '25', '26', '27', '28', '29', '210', '211', '212',
                                        #'213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230',
                                        #'231', '232', '233', '234', '235', '31', '33', '35'])
    
    def handle(self, handler_input):
        logger.info("In YesIntentHandler")
        logger.info(str(handler_input))
        state = handler_input.attributes_manager.session_attributes['test_state']
        if state['item'] == MEMORY:
            if state['step'] == 1:
                state['step'] = 2
                return handler_input.response_builder.speak(TEST['memory'][1]['speak']).ask(TEST['memory'][1]['reprompt']).response

        elif state['item'] == ATTENTION:
            if state['step'] == 1:
                state['step'] = 2
                return handler_input.response_builder.speak(TEST['attention'][1]['speak']).ask(TEST['attention'][1]['reprompt']).response
            elif state['step'] == 3:
                state['step'] = 4
                return handler_input.response_builder.speak(TEST['attention'][3]['speak']).ask(TEST['attention'][3]['reprompt']).response
            elif state['step'] == 5:
                state['step'] = 6
                state['letters_last_time'] = str(time.time())
                return handler_input.response_builder.speak(TEST['attention'][5]['speak']).ask(TEST['attention'][5]['reprompt']).response
            elif state['step'] >= 6 and state['step'] <= 34:#14
                elapsed = time.time() - float(state['letters_last_time'])
                if elapsed <= TIME_THRESHOLD and LETTERS[state['step']-6] == 'A':
                    state['letter_mistakes'] -= 1
                state['step'] += 1
                state['letters_last_time'] = str(time.time())
                return handler_input.response_builder.speak(TEST['attention'][state['step']-1]['speak']).ask(TEST['attention'][state['step']-1]['reprompt']).response
            elif state['step'] == 35:#15
                state['step'] = 36#16
                return handler_input.response_builder.speak(TEST['attention'][35]['speak']).ask(TEST['attention'][35]['reprompt']).response#[15]
        
        elif state['item'] == LANGUAGE:
            if state['step'] == 1:
                state['step'] = 2
                return handler_input.response_builder.speak(TEST['language'][1]['speak']).ask(TEST['language'][1]['reprompt']).response
            elif state['step'] == 3:
                state['step'] = 4
                return handler_input.response_builder.speak(TEST['language'][3]['speak']).ask(TEST['language'][3]['reprompt']).response
            elif state['step'] == 5:
                state['step'] = 6
                state['f_start_time'] = str(time.time())
                return handler_input.response_builder.speak(TEST['language'][5]['speak']).ask(TEST['language'][5]['reprompt']).response

        return NextIntentHandler().handle(handler_input)


class NoIntentHandler(AbstractRequestHandler):
    """Handler for No Intent"""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In NoIntentHandler")
        logger.info(str(handler_input))
        state = handler_input.attributes_manager.session_attributes['test_state']
        if state['item'] == MEMORY:
            if state['step'] == 1:
                return RepeatIntentHandler().handle(handler_input)

        elif state['item'] == ATTENTION:
            if state['step'] in [1, 3, 5, 35]:#15
                return RepeatIntentHandler().handle(handler_input)
            elif state['step'] >= 6 and state['step'] <= 34:#14
                elapsed = time.time() - float(state['letters_last_time'])
                if elapsed <= TIME_THRESHOLD and LETTERS[state['step']-6] != 'A':
                    state['letter_mistakes'] -= 1
                state['step'] += 1
                state['letters_last_time'] = str(time.time())
                return handler_input.response_builder.speak(TEST['attention'][state['step']-1]['speak']).ask(TEST['attention'][state['step']-1]['reprompt']).response
        
        elif state['item'] == LANGUAGE:
            if state['step'] in [1, 3, 5]:
                return RepeatIntentHandler().handle(handler_input)

        return NextIntentHandler().handle(handler_input) # By default, if users says "no", we go to the next step


class DigitListIntentHandler(AbstractRequestHandler):
    """Handler for Digit List Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("DigitListIntent")(handler_input) and full_state in ['24', '22'])
    
    def handle(self, handler_input):
        logger.info("In DigitListIntentHandler")
        state = handler_input.attributes_manager.session_attributes['test_state']
        if state['item'] == ATTENTION:
            if state['step'] == 2:
                state['forward_numbers'] = 1
            elif state['step'] == 4:
                state['backward_numbers'] = 1

        return NextIntentHandler().handle(handler_input)


class NumbersIntentHandler(AbstractRequestHandler):
    """Handler for Numbers Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("NumbersIntent")(handler_input) and full_state in ['22', '24', '216', '61', '63', '64', '236'])
    
    def handle(self, handler_input):
        logger.info("In NumbersIntentHandler")
        state = handler_input.attributes_manager.session_attributes['test_state']
        slots = handler_input.request_envelope.request.intent.slots
        if state['item'] == ATTENTION:
            if state['step'] == 2:
                if slots['numero_uno'].value == '2' and slots['numero_dos'].value == '1' and slots['numero_tres'].value == '8' and slots['numero_cuatro'].value == '5' and slots['numero_cinco'].value == '4':
                    state['forward_numbers'] = 1
                return NextIntentHandler().handle(handler_input)

            elif state['step'] == 4:
                if slots['numero_uno'].value == '2' and slots['numero_dos'].value == '4' and slots['numero_tres'].value == '7':
                    state['backward_numbers'] = 1
                return NextIntentHandler().handle(handler_input)
                
            elif state['step'] == 36:#16
                state['calculations'] += [int(slots[num].value) for num in slots if (slots[num].value is not None and slots[num].value.isdigit())]

                if len(state['calculations']) >= 5:
                    # NEXT
                    state['item'] = LANGUAGE
                    state['step'] = 1
                    return handler_input.response_builder.speak(TEST["language"][0]["speak"]).ask(TEST["language"][0]["reprompt"]).response
                else:
                    return handler_input.response_builder.speak('Continúe').ask('<prosody rate="slow"><p>Continúe</p></prosody>').response

        elif state['item'] == ORIENTATION:
            if state['step'] == 1:
                state['day'] = int(slots['numero_uno'].value)
            elif state['step'] == 3:
                state['month'] = int(slots['numero_uno'].value)
            elif state['step'] == 4:
                state['year'] = int(slots['numero_uno'].value)
            return NextIntentHandler().handle(handler_input)


class FirstSentenceIntentHandler(AbstractRequestHandler):
    """Handler for First Sentence Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("FirstSentenceIntent")(handler_input) and full_state in ['32'])
    
    def handle(self, handler_input):
        logger.info("In FirstSentenceIntentHandler")
        handler_input.attributes_manager.session_attributes['test_state']['first_sentence'] = 1
        return NextIntentHandler().handle(handler_input)


class SecondSentenceIntentHandler(AbstractRequestHandler):
    """Handler for Second Sentence Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("SecondSentenceIntent")(handler_input) and full_state in ['34'])
    
    def handle(self, handler_input):
        logger.info("In SecondSentenceIntent")
        handler_input.attributes_manager.session_attributes['test_state']['second_sentence'] = 1
        return NextIntentHandler().handle(handler_input)


class TransporteIntentHandler(AbstractRequestHandler):
    """Handler for Transporte Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("TransporteIntent")(handler_input) and full_state in ['42'])
    
    def handle(self, handler_input):
        logger.info("In TransporteIntentHandler")
        handler_input.attributes_manager.session_attributes['test_state']['transport'] = 1
        return NextIntentHandler().handle(handler_input)


class MedirIntentHandler(AbstractRequestHandler):
    """Handler for Medir Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("MedirIntent")(handler_input) and full_state in ['43'])
    
    def handle(self, handler_input):
        logger.info("In MedirIntentHandler")
        handler_input.attributes_manager.session_attributes['test_state']['measure'] = 1
        return NextIntentHandler().handle(handler_input)


class SemanaIntentHandler(AbstractRequestHandler):
    """Handler for Semana Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("SemanaIntent")(handler_input) and full_state in ['62'])
    
    def handle(self, handler_input):
        
        logger.info("In SemanaIntentHandler")
        state = handler_input.attributes_manager.session_attributes['test_state']
        state['week'] = handler_input.request_envelope.request.intent.slots['dia'].value
        return NextIntentHandler().handle(handler_input)


class MesIntentHandler(AbstractRequestHandler):
    """Handler for Mes Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("MesIntent")(handler_input) and full_state in ['63'])
    
    def handle(self, handler_input):
        
        logger.info("In MesIntentHandler")
        state = handler_input.attributes_manager.session_attributes['test_state']
        state['month'] = handler_input.request_envelope.request.intent.slots['mes'].value
        return NextIntentHandler().handle(handler_input)


class VigoIntentHandler(AbstractRequestHandler):
    """Handler for Vigo Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("VigoIntent")(handler_input) and full_state in ['66'])
    
    def handle(self, handler_input):
        logger.info("In VigoIntentHandler")
        handler_input.attributes_manager.session_attributes['test_state']['vigo'] = 1
        return NextIntentHandler().handle(handler_input)


class AfagaIntentHandler(AbstractRequestHandler):
    """Handler for Afaga Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("AfagaIntent")(handler_input) and full_state in ['65'])
    
    def handle(self, handler_input):
        handler_input.attributes_manager.session_attributes['test_state']['afaga'] = 1
        return NextIntentHandler().handle(handler_input)


class FWordIntentHandler(AbstractRequestHandler):
    """Handler for F Word Intent"""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FWordIntent")(handler_input)
    
    def handle(self, handler_input):
        logger.info("In NextIntentHandler")
        state = handler_input.attributes_manager.session_attributes['test_state']
        slots = handler_input.request_envelope.request.intent.slots
        if state['item'] == LANGUAGE:
            if state['step'] == 6:
                state['f_words'] += [slots[word].value for word in slots if (slots[word].value in F_WORDS)]

                if ((time.time() - float(state['f_start_time']) < 68.0) and (len(set(state['f_words'])) < 11)): # Around 60 seconds to say 11 f words
                    return handler_input.response_builder.speak('Siga').ask('Continúe').response
                else:
                    state['item'] = ABSTRACTION
                    state['step'] = 1
                    return handler_input.response_builder.speak('''<prosody rate="slow"><p>Gracias, con eso es suficiente. </p></prosody>''' + TEST['abstraction'][0]['speak']).ask(TEST['abstraction'][0]['reprompt']).response

        return NextIntentHandler().handle(handler_input)


class NextIntentHandler(AbstractRequestHandler):
    """Handler for Next Intent"""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.NextIntent")(handler_input)
    
    def handle(self, handler_input):
        
        logger.info("In NextIntentHandler")
        state = handler_input.attributes_manager.session_attributes['test_state']
        item = list(TEST)[state['item']]
        step = state['step']
        
        session_attr = handler_input.attributes_manager.session_attributes
        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()


        state['letters_last_time'] = str(time.time())
        state['f_start_time'] = str(time.time())

        if step < len(TEST[item]):
            state['step'] += 1
            return handler_input.response_builder.speak(TEST[item][step]["speak"]).ask(TEST[item][step]["reprompt"]).response
        elif state['item'] != ORIENTATION:
            state['item'] += 1
            state['step'] = 1
            nextItem = list(TEST)[state['item']]
            return handler_input.response_builder.speak(TEST[nextItem][0]["speak"]).ask(TEST[nextItem][0]["reprompt"]).response
        else:
            return handler_input.response_builder.speak('''<prosody rate="slow"><p>Hemos terminado. Lo has hecho muy bien! Muchas gracias!</p></prosody>''').response


class RepeatIntentHandler(AbstractRequestHandler):
    """Handler for Repeat Intent"""
    def can_handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        full_state = str(state['item']) + str(state['step'])
        return (ask_utils.is_intent_name("AMAZON.RepeatIntent")(handler_input) and full_state in ['11', '21', '23', '25', '215', '31', '33', '35', '41', '42', '43', '51', '61', '62', '63', '64', '65', '66', '235'])
    
    def handle(self, handler_input):
        state = handler_input.attributes_manager.session_attributes['test_state']
        item = list(TEST)[state['item']]
        step = state['step']
        session_attr = handler_input.attributes_manager.session_attributes
        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()
        return handler_input.response_builder.speak(TEST[item][step-1]["speak"]).ask(TEST[item][step-1]["reprompt"]).response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        session_attr = handler_input.attributes_manager.session_attributes
        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()
        return RepeatIntentHandler().handle(handler_input)


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")
        session_attr = handler_input.attributes_manager.session_attributes
        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()
        return handler_input.response_builder.speak('''<prosody rate="slow"><p>El test ha sido pausado</p></prosody>''').response


class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        
        state = handler_input.attributes_manager.session_attributes['test_state']
        if state['item'] == LANGUAGE:
            if state['step'] == 6:
                if (time.time() - float(state['f_start_time'])) < 68.0: # Around 60 seconds to say f words
                    return handler_input.response_builder.speak('Continúe').ask('Continúe.').response
                else:
                    state['item'] = ABSTRACTION
                    state['step'] = 1
                    return handler_input.response_builder.speak('''<prosody rate="slow"><p>Gracias, con eso es suficiente. </p></prosody>''' + TEST['abstraction'][0]['speak']).ask(TEST['abstraction'][0]['reprompt']).response

        return NextIntentHandler().handle(handler_input)


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        session_attr = handler_input.attributes_manager.session_attributes
        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "Acaba de activar " + intent_name + "."

        session_attr = handler_input.attributes_manager.session_attributes
        handler_input.attributes_manager.persistent_attributes = session_attr
        handler_input.attributes_manager.save_persistent_attributes()
        
        return NextIntentHandler().handle(handler_input)
        #return (
        #    handler_input.response_builder
        #        .speak(speak_output)
                #.ask("add a reprompt if you want to keep the session open for the user to respond")
        #        .response
        #)


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Perdone, he tenido un problema para hacer esto."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = CustomSkillBuilder(persistence_adapter = dynamodb_adapter)

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(RememberIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(DigitListIntentHandler())
sb.add_request_handler(FirstSentenceIntentHandler())
sb.add_request_handler(SecondSentenceIntentHandler())
sb.add_request_handler(TransporteIntentHandler())
sb.add_request_handler(MedirIntentHandler())
sb.add_request_handler(SemanaIntentHandler())
sb.add_request_handler(MesIntentHandler())
sb.add_request_handler(AfagaIntentHandler())
sb.add_request_handler(VigoIntentHandler())
sb.add_request_handler(NumbersIntentHandler())
sb.add_request_handler(FWordIntentHandler())
sb.add_request_handler(NextIntentHandler())
sb.add_request_handler(RepeatIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()