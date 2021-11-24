# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import datetime as dt

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class cekFormulir(Action):

    def name(self) -> Text:
        return "action_cek_formulir"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        teks_asal = ""
        teks_tujuan = ""
        teks = "kosong"
        teks2 = "kosong2"
        halaman = "0"
        for e in entities:
            if e['entity'] == 'isi_formulir':
                teks = e['value']
                if teks == 'penghuni asrama' or teks == "asrama":
                    dispatcher.utter_message(text="Untuk Formulir penghuni asrama Terdapat pada buku pedoman akademik halaman 81")
                elif teks == 'pengunduran diri' or teks == "pengunduran":
                    dispatcher.utter_message(text="Untuk Formulir pengunduran diri Terdapat pada buku pedoman akademik halaman 83")
                elif teks == 'mengikuti wisuda' or teks == "wisuda":
                    dispatcher.utter_message(text="Untuk Biodata mengikuti wisuda Terdapat pada buku pedoman akademik halaman 87")
                elif teks == 'alumni':
                    dispatcher.utter_message(text="Untuk Biodata akademik alumni Terdapat pada buku pedoman akademik halaman 88")
                
            if teks == "perpindahan" and e['entity'] == 'tipe_permohonan':
                teks2 = e['value']
                if teks2 == 'program studi' or teks2 == "prodi":
                    dispatcher.utter_message(text="Untuk Formulir permohonan perpindahan antar program studi Terdapat pada buku pedoman akademik halaman 84")
                elif teks2 == 'universitas sriwijaya' or teks2 == "unsri":
                    dispatcher.utter_message(text="Untuk Formulir permohonan perpindahan dari universitas sriwijaya ke perguruan tinggi lain Terdapat pada buku pedoman akademik halaman 86")
                elif teks2 == 'perguruan tinggi lain' or teks2 == "ptn lain":
                    dispatcher.utter_message(text="Untuk Formulir permohonan perpindahan dari perguruan tinggi lain ke universitas sriwijaya Terdapat pada buku pedoman akademik halaman 85")
        
        if teks == "kosong":
            dispatcher.utter_message(text="Formulir tidak tersedia")

        return []

class ActionBeriWaktu(Action):

    def name(self) -> Text:
        return "action_beri_waktu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        x = dt.datetime.now()

        for e in entities:
            if e['entity'] == 'waktu':
                dispatcher.utter_message(text=f"Jam sekarang : {x.strftime('%X')}")
            if e['entity'] == 'tanggal':
                dispatcher.utter_message(text=f"Tanggal sekarang : {x.strftime('%x')}")
            if e['entity'] == 'hari':
                dispatcher.utter_message(text=f"Hari sekarang : {x.strftime('%A')}")

        return []
