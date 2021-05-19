from typing import Dict, Text, List, Optional, Any

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.events import AllSlotsReset, SlotSet, SessionStarted, UserUtteranceReverted
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict
import json
import pandas as pd
from pandas import json_normalize
import datetime
import requests
import random
import pygsheets
# show projects


def gettoken():
    url = "https://bim.constology.com/api/auth/login"
    body = {"email": "hassan@constology.com", "password": "hassan"}
    x = requests.post(url, data=json.dumps(body), headers={
                      'Content-Type': 'application/json'})
    print(x.json())
    return x.json()['Authorization']


class ValidateProjectForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_project_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_phone_system(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("phone_system") == None:
            print("Proejctssss count")
            return {"phone_system": None}
        else:
            print("Proejctssss count")
            return {"phone_system": slot_value}
    
    def validate_brand_system(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("brand_system") == None:
            return {"brand_system": None}
        else:
         
            return {"brand_system": slot_value}

    def validate_possible_communications(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("possible_communications") == None:
            return {"possible_communications": None}
        else:
         
            return {"possible_communications": slot_value}

    def validate_what_industry(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("what_industry") == None:
            return {"what_industry": None}
        else:
         
            return {"what_industry": slot_value} 

    def validate_many_phones(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("many_phones") == None:
            return {"many_phones": None}
        else:
         
            return {"many_phones": slot_value} 

    def validate_multiple_locations(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("multiple_locations") == None:
            return {"multiple_locations": None}
        else:
         
            return {"multiple_locations": slot_value}  

    def validate_many_people(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("many_people") == None:
            return {"many_people": None}
        else:
         
            return {"many_people": slot_value} 

    def validate_website_address(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("website_address") == None:
            return {"website_address": None}
        else:
         
            return {"website_address": slot_value} 

    def validate_more_items(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("more_items") == None:
            return {"more_items": None}
        else:
         
            return {"more_items": slot_value} 

    def validate_come_to_Quoteaphone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("come_to_Quoteaphone") == None:
            return {"come_to_Quoteaphone": None}
        else:
         
            return {"come_to_Quoteaphone": slot_value}  

    def validate_premier_industry(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("premier_industry") == None:
            return {"premier_industry": None}
        else:
         
            return {"premier_industry": slot_value}

    def validate_following_information(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("following_information") == None:
            return {"following_information": None}
        else:
         
            return {"following_information": slot_value}

    def validate_First_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("First_name") == None:
            return {"First_name": None}
        else:
         
            return {"First_name": slot_value}  

    def validate_Last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("Last_name") == None:
            return {"Last_name": None}
        else:
         
            return {"Last_name": slot_value} 

    def validate_Business_Title(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("Business_Title") == None:
            return {"Business_Title": None}
        else:
         
            return {"Business_Title": slot_value}

    def validate_Company_Name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("Company_Name") == None:
            return {"Company_Name": None}
        else:
         
            return {"Company_Name": slot_value}

    def validate_Email_user(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("Email_user") == None:
            return {"Email_user": None}
        else:
         
            return {"Email_user": slot_value}                                     

    def validate_Phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("Phone_number") == None:
            return {"Phone_number": None}
        else:
         
            return {"Phone_number": slot_value}

    def validate_Address_user(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("Address_user") == None:
            return {"Address_user": None}
        else:
         
            return {"Address_user": slot_value}

    def validate_city_user(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("city_user") == None:
            return {"city_user": None}
        else:
         
            return {"city_user": slot_value}

    def validate_state_user(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("state_user") == None:
            return {"state_user": None}
        else:
         
            return {"state_user": slot_value}

    def validate_zip_user(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if tracker.get_slot("zip_user") == None:
            return {"zip_user": None}
        else:
         
            return {"zip_user": slot_value}                                

class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "action_submitproject"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Thanks for talking with me.  I’m going to zip this information right into our consulting department to get your price to you within the next 48 hours.  Thanks for getting your quote from Quoteaphone!   Quote-Wiz")
        view_count_project = tracker.get_slot("phone_system")
        print(view_count_project)
        gc = pygsheets.authorize()
        sh = gc.open('bot_sheet')
        wks = sh.sheet1
        wks.append_table(values=[tracker.get_slot("phone_system"),tracker.get_slot("brand_system"),tracker.get_slot("possible_communications"),tracker.get_slot("what_industry"),tracker.get_slot("many_phones"),tracker.get_slot("multiple_locations"),tracker.get_slot("many_people"),tracker.get_slot("website_address"),tracker.get_slot("more_items"),tracker.get_slot("come_to_Quoteaphone"),tracker.get_slot("premier_industry"),tracker.get_slot("following_information"),tracker.get_slot("First_name"),tracker.get_slot("Last_name"),tracker.get_slot("Business_Title"),tracker.get_slot("Company_Name"),tracker.get_slot("Email_user"),tracker.get_slot("Phone_number"),tracker.get_slot("Address_user"),tracker.get_slot("city_user"),tracker.get_slot("state_user"),tracker.get_slot("zip_user")])
        

        return[SlotSet("phone_system", None)]

##########################################################################################

# show sections for projects


class ValidateSectionFormproj(FormValidationAction):
    def name(self) -> Text:
        return "validate_show_sectionforproject_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_sectionsperprojectid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            return {"sectionsperprojectid": None}
        else:
            return {"sectionsperprojectid": slot_value}


class ActionSubmitSection(Action):
    def name(self) -> Text:
        return "action_submishowtsectionforproject"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            "Thank for providing details. Fetching results....")
        # diary_date = date(tracker.get_slot("date"))  #yyyymmdd  #or datetime
        diary_section_id = tracker.get_slot("sectionsperprojectid")
        #diary_section_id = diary_section_id[-1]
        if(isinstance(diary_section_id, list)):
            diary_section_id = diary_section_id[-1]

        # diary_section_id = "proj-A testA"   #proj-A testA
        print('Sect slot value is : ', diary_section_id)
        token = gettoken()
        headers = {'Authorization': token,
                   'Content-type': 'application/json', }
        # p_url='https://bim.constology.com/api/project'
        p_url = 'https://bim.constology.com/api/project'
        x = requests.get(p_url, headers=headers)
        projects = (x.json()['data'])
        prj = None
        print(projects)
        for item in projects:
            print(item)
            if item['name'] == diary_section_id:
                prj = item
        print('Selected Project is : ', prj)
        diary_url = 'https://bim.constology.com/api/section/p/' + \
            prj['public_id']
        diary = requests.get(diary_url, headers=headers)
        print(diary.json())
        data_fetched = diary.json()
        dispatcher.utter_message("Opening Sections.... ")

        #dispatcher.utter_message(json.dumps(data_fetched, indent=1))

        # converting json into dataframe
        df = json_normalize(data_fetched)
        print(df)
        #df_sections = df.loc[:,['id','title','date','weather_degree','weather_wind_speed','weather_rain','section_public_id']]
        #df_sections = df.loc[:,['name','code']]
        # print(df_sections)
        #df_sections = df_sections.to_dict()
        df_sections = df.to_dict()
        # print(df_sections)
        dispatcher.utter_message(json.dumps(df_sections, indent=1))
        return [SlotSet('sectionsperprojectid', None)]


##########################################################################################
# show all sections
class ValidateSectionForm(Action):
    def name(self) -> Text:
        return "validate_section_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_sections_count(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            return {"sections_count": None}
        else:
            return {"sections_count": slot_value}


class ActionSubmitSectionn(Action):
    def name(self) -> Text:
        return "action_submitsection"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        view_count_section = tracker.get_slot("sections_count")
        view_count_section = int(view_count_section)
        # dispatcher.utter_message(template="utter_details_thanks")
        url = "https://bim.constology.com/api/section"
        token = gettoken()
        headers = {'Authorization': token, 'Content-type': 'application/json'}
        x = requests.get(url, headers=headers)
        # print(x.json())
        print(x.json()['data'])
        data_fetched = x.json()['data']
        #data_fetched = x.json()
        dispatcher.utter_message("sections fetching....")

        # converting json into dataframe
        df = json_normalize(data_fetched)
        # print(df)
        df_sections = df.loc[:, ['code', 'name']]

        total = df_sections['name'].count()
        dispatcher.utter_message("Total number of Sections are :")
        dispatcher.utter_message(json.dumps(str(total), indent=1))

        #print("total number of sections: ",total)
        if total >= 5:
            #print("There are more than 5 sections. How many you want to view.")
            dispatcher.utter_message(
                "Below are the number of Sections as per your request.")

        print(view_count_section)
        # print(df_sections['name'])
        total_projects = df_sections['name'][:view_count_section]
        print(total_projects)
        total = total_projects.to_dict()
        print(total)

        #df_sections = df_sections.to_dict()
        # print(df_sections)

        dispatcher.utter_message(json.dumps(total, indent=1))

        return[SlotSet("sections_count", view_count_section)]


# show diary (all diaries)
class ValidateDiaryForm(Action):
    def name(self) -> Text:
        return "validate_diary_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_diaries_count(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            return {"diaries_count": None}
        else:
            return {"diaries_count": slot_value}


class ActionSubmitDiary(Action):
    def name(self) -> Text:
        return "action_submitdiary"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        view_count_diary = tracker.get_slot("diaries_count")
        view_count_diary = int(view_count_diary)
        # dispatcher.utter_message(template="utter_details_thanks")
        url = "https://bim.constology.com/api/diary/"
        token = gettoken()
        headers = {'Authorization': token, 'Content-type': 'application/json'}
        x = requests.get(url, headers=headers)
        # print(x.json())
        print(x.json()['data'])
        data_fetched = x.json()['data']
        #data_fetched = x.json()
        dispatcher.utter_message("Diaries fetching....")

        # converting json into dataframe
        df = json_normalize(data_fetched)
        # print(df)
        df_sections = df.loc[:, ['title', 'date']]

        total = df_sections['title'].count()
        dispatcher.utter_message("Total number of Diaries are :")
        dispatcher.utter_message(json.dumps(str(total), indent=1))

        #print("total number of sections: ",total)
        if total >= 5:
            #print("There are more than 5 sections. How many you want to view.")
            dispatcher.utter_message(
                "Below are the number of Diaries as per your request.")

        print(view_count_diary)
        # print(df_sections['name'])
        total_projects = df_sections['title'][:view_count_diary]
        print(total_projects)
        total = total_projects.to_dict()
        print(total)

        #df_sections = df_sections.to_dict()
        # print(df_sections)

        dispatcher.utter_message(json.dumps(total, indent=1))

        return[SlotSet("diaries_count", view_count_diary)]


# create diary by filling
class ValidateCreateDiaryForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_create_diary_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_section_old(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            print("111111111111111")
            return {"section_old": None}
        else:
            return {"section_old": slot_value}

    def validate_title_old(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            print("222222222222222222222")
            return {"title_old": None}
        else:
            return {"title_old": slot_value}

    def validate_date_old(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            return {"date_old": None}
        else:
            return {"date_old": slot_value}


class ActionSubmitCreateDiary(Action):
    def name(self) -> Text:
        return "action_submitcreatediary"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        #view_count_project = tracker.get_slot("projects_count")
        d_section = tracker.get_slot("section_old")[-1]
        d_title = tracker.get_slot("title_old")[-1]
        d_date = tracker.get_slot("date_old")[-1]
        d_is_active = bool("true")
        print("title of diary is :", d_title)
        print("date of diary is :", d_date)
        print("Section is :", d_section)
        token = gettoken()
        headers = {'Authorization': token, 'Content-type': 'application/json'}
        p_url = 'https://bim.constology.com/api/section'
        x = requests.get(p_url, headers=headers)
        projects = (x.json()['data'])
        prj = None
        for item in projects:
         # print(item)
            if item['name'] == d_section:
                prj = item
        print('Selected section is : ', prj)

        dispatcher.utter_message("Thanks, your answers have been recorded!")
        url = 'https://bim.constology.com/api/diary/'
        #dt = {"title": d_title, "date": d_date, "section": d_section}
        dt = {"id": "", "title": d_title, "date": d_date, "weather_degree": " ", "weather_wind_speed": " ", "weather_rain": " ",
              "weather_img": " ", "section_public_id": prj['public_id'], "public_id": " ", "is_active": d_is_active}
        print(dt)
        token = gettoken()
        headers = {'Authorization': token, 'Content-type': 'application/json'}
        x = requests.post(url, json=dt, headers=headers)
        print(x, x.text)
        dispatcher.utter_message("Created Diary Successfully.. ")
        return []


# show diaries for project
# Open diary  project id required  :  for testing use : c1c48cb9-52eb-4efd-92e3-e2f707437514,
class ValidateOpenDiaryForm(Action):
    def name(self) -> Text:
        return "validate_open_diary_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_projectid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            return {"projectid": None}
        else:
            return {"projectid": slot_value}


class ActionOpenDiary(Action):
    def name(self) -> Text:
        return "action_opendiary"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            "Thank for providing details. Fetching results....")
        # diary_date = date(tracker.get_slot("date"))  #yyyymmdd  #or datetime
        diary_section_id = str(tracker.get_slot("projectid"))
        token = gettoken()
        headers = {'Authorization': token,
                   'Content-type': 'application/json', }
        p_url = 'https://bim.constology.com/api/project'
        x = requests.get(p_url, headers=headers)
        projects = (x.json()['data'])
        prj = None
        for item in projects:
            # print(item)
            if item['name'] == diary_section_id:
                prj = item
        print('Selected Project is : ', prj)
        diary_url = 'https://bim.constology.com/api/diary/project/' + \
            prj['public_id']
        diary = requests.get(diary_url, headers=headers)
        print(diary.json())
        data_fetched = diary.json()
        dispatcher.utter_message("Opening diaries.... ")

        #dispatcher.utter_message(json.dumps(data_fetched, indent=1))

        # converting json into dataframe
        df = json_normalize(data_fetched)
        print(df)
        #df_sections = df.loc[:,['id','title','date','weather_degree','weather_wind_speed','weather_rain','section_public_id']]
        df_sections = df.loc[:, ['title', 'date']]
        # print(df_sections)
        df_sections = df_sections.to_dict()
        # print(df_sections)
        dispatcher.utter_message(json.dumps(df_sections, indent=1))
        return []


# show diaries for sections
class ValidateOpenDiaryFormsection(FormValidationAction):
    def name(self) -> Text:
        return "validate_show_diaryforsection_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_diarieispersectiontid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            return {"diarieispersectiontid": None}
        else:
            return {"diarieispersectiontid": slot_value}


class ActionOpenDiarysection(Action):
    def name(self) -> Text:
        return "action_submitshowdiaryforsection"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            "Thank for providing details. Fetching results....")
        # diary_date = date(tracker.get_slot("date"))  #yyyymmdd  #or datetime
        diary_section_id = tracker.get_slot("diarieispersectiontid")
        if(isinstance(diary_section_id, list)):
            diary_section_id = diary_section_id[0]
        else:
            diary_section_id = diary_section_id
        # diary_section_id = "proj-A testA"   #proj-A testA
        print('slot value is : ', diary_section_id)
        token = gettoken()
        headers = {'Authorization': token,
                   'Content-type': 'application/json', }
        # p_url='https://bim.constology.com/api/project'
        p_url = 'https://bim.constology.com/api/section'
        x = requests.get(p_url, headers=headers)
        projects = (x.json()['data'])
        prj = None
        for item in projects:
            print(item, "===dwd", diary_section_id)
            if item['name'] == diary_section_id:
                prj = item
        if prj == None:
            dispatcher.utter_message("This sections doesnt exist")
            return [SlotSet("diarieispersectiontid", None)]
        print('Selected Project is : ', prj)
        diary_url = 'https://bim.constology.com/api/diary/section/' + \
            prj['public_id']
        diary = requests.get(diary_url, headers=headers)
        print(diary.json())
        data_fetched = diary.json()
        dispatcher.utter_message("Opening diaries.... ")

        #dispatcher.utter_message(json.dumps(data_fetched, indent=1))

        # converting json into dataframe
        df = json_normalize(data_fetched)
        print(df)
        #df_sections = df.loc[:,['id','title','date','weather_degree','weather_wind_speed','weather_rain','section_public_id']]
        df_sections = df.loc[:, ['title', 'date']]
        # print(df_sections)
        df_sections = df_sections.to_dict()
        # print(df_sections)
        dispatcher.utter_message(json.dumps(df_sections, indent=1))
        return [SlotSet("diarieispersectiontid", None)]


# show diaries for projects
class ValidateOpenDiaryFormproj(FormValidationAction):
    def name(self) -> Text:
        print("diary for project=====dsdsd")
        return "validate_show_diaryforproject_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker.get_slot("diarieisperprojectid"), "========MM=========")
        return []

    def validate_diarieispersectiontid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        print(tracker.get_slot("diarieisperprojectid"), "=================")
        if tracker.get_slot("diarieisperprojectid") == None:
            return {"diarieisperprojectid": None}
        else:
            return {"diarieisperprojectid": slot_value}

    def validate_diarieslimit(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        if not slot_value:
            return {"diarieslimit": None}
        else:
            return {"diarieslimit": slot_value}


class ActionOpenDiaryProj(Action):
    def name(self) -> Text:
        return "action_submitshowdiaryforproject"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            "Thank for providing details. Fetching results....")
        # diary_date = date(tracker.get_slot("date"))  #yyyymmdd  #or datetime
        diary_section_id = tracker.get_slot("diarieisperprojectid")
        limit_diary = tracker.get_slot("diarieslimit")
        if(isinstance(diary_section_id, list)):
            diary_section_id = diary_section_id[-1]
        if(isinstance(limit_diary, list)):
            try:
                limit_diary = int(limit_diary[-1])
            except:
                print("all diaries")
        else:
            limit_diary = int(limit_diary)

        # diary_section_id = "proj-A testA"   #proj-A testA
        print('proj slot value is : ', diary_section_id, limit_diary)
        token = gettoken()
        headers = {'Authorization': token,
                   'Content-type': 'application/json', }
        p_url = 'https://bim.constology.com/api/project'
        # p_url='https://bim.constology.com/api/section'
        x = requests.get(p_url, headers=headers)
        projects = (x.json()['data'])
        prj = None
        for item in projects:
            # print(item)
            print(item['name'], diary_section_id)
            if item['name'] == diary_section_id:
                prj = item
        print('Selected Project is : ', prj)
        diary_url = 'https://bim.constology.com/api/diary/project/' + \
            prj['public_id']
        diary = requests.get(diary_url, headers=headers)
        print(diary.json())
        data_fetched = diary.json()
        if(len(data_fetched) > limit_diary):
            data_fetched = data_fetched[:limit_diary]
        dispatcher.utter_message("Opening diaries.... ")

        #dispatcher.utter_message(json.dumps(data_fetched, indent=1))

        # converting json into dataframe
        df = json_normalize(data_fetched)
        print(df)
        #df_sections = df.loc[:,['id','title','date','weather_degree','weather_wind_speed','weather_rain','section_public_id']]
        df_sections = df.loc[:, ['title', 'date']]
        # print(df_sections)
        df_sections = df_sections.to_dict()
        # print(df_sections)
        dispatcher.utter_message(json.dumps(df_sections, indent=1))
        return [SlotSet("diarieisperprojectid", None)]
