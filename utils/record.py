import asyncio
from s2txt import AppAPI as api
from config import Config

class Record_:

    async def insertTask(self):
    	# No try: ... except: ... !
        spec = 0
        while True:
            # from configs

            sourcev = await api.s2txt_google(device_index=Config().get("mic"), language=Config().get("lang"), timeout=Config().get("rtimeout"), clear_voice=Config().get("rclear_voice"), phrase_time_limit=Config().get("rphrase_timeout"))
            # sourcev = await api.s2txt_vosk(device_index=Config().get("mic"))
            # sourcev = "txt"

            if not sourcev.startswith("SPErr0") and sourcev != None:
                self.label_google_exceptions.setText(".")
                await asyncio.sleep(1)
                self.textEdit.insertPlainText(" " + sourcev)
                self.label_google_exceptions.setText("...")
            else:
                if sourcev.startswith("SPErr04"):
                    self.WarningUi(
                        "Вы выбрали верное устройство для ввода звука?")
                    self.recordButton.click()
                    break
                else:
                    spec += 1
                    self.label_google_exceptions.setText("!")
                    await asyncio.sleep(1)
                    self.label_google_exceptions.setText(f"{sourcev[9::]} ({str(spec)})")
                    await asyncio.sleep(1)
                    self.label_google_exceptions.setText("...")

            # self.recordButton.setText("Запись")
            # self.recordButton.toggle()
            # self.action_r_start.setEnabled(True)
            # self.action_r_stop.setEnabled(False)
            self.recordButton.setShortcut(self.shortcut_btn_record)

    def Record(self):
        try:
            if self.recordButton.isChecked():  # ... + errors handler \/
                if self.recordButton.text() != "Стоп":
                    self.recordButton.setText("Стоп")
                    self.action_r_stop.setEnabled(True)
                    self.action_r_start.setEnabled(False)
                    self.recordButton.setShortcut(self.shortcut_btn_record)
                    # self.recordButton.repaint()

                    self.ltask = asyncio.create_task(self.insertTask())
                    self.label_google_exceptions.setText("...")
                    # await self.insertTask()

                ###
            else:
                # print("STOP!")
                self.ltask.cancel()
                self.label_google_exceptions.setText("Начните запись")
                self.recordButton.setText("Запись")
                self.action_r_stop.setEnabled(False)
                self.action_r_start.setEnabled(True)
                self.recordButton.setShortcut(self.shortcut_btn_record)
                # self.recordButton.toggle()

        except Exception as err:
            # self.recordButton.toggle()
            self.recordButton.setText("Запись")
            self.recordButton.setShortcut(self.shortcut_btn_record)
            # self.recordButton.repaint()
            self.CriticalUi(str(err))

