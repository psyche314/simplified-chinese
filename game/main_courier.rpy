default in_cooldown_jobs = {}
default courier_board = []
default active_deliveries = []
default last_courier_refresh_day = 0
default reacher = 0
default haimo_dialogue = {"Encounter": 0, "Questions": {}}
default courier_stats = {}
default max_rank = 7

init python:

    courier_jobs = {
        "Settling the Debt": {
            "client": ["Sebas"],
            "recipient": ["Cane"],
            "package": [{"Gold": 50}],
            "minimum rank": 2,
            "cooldown days": 3,
            "expire days": 7,
            "reward": {"Gold": 10, "Reputation": 5},
            "description": "Pay back 50 Gold of debt for Sebas to Cane."
        },
        "Tending New Wounds": {
            "client": ["Ole"],
            "recipient": ["Jog", "Lothar"],
            "package": [{"Green Ointment": 1}],
            "minimum rank": 1,
            "cooldown days": 2,
            "expire days": 7,
            "reward": {"Gold": 8, "Reputation": 8},
            "description": "Deliver a speedy remedy for Ole."
        },
        "Adventure Discovery": {
            "client": ["Lothar"],
            "recipient": ["Rahim"],
            "package": [{"Strap": 2}, {"Small Cloth": 2}],
            "minimum rank": 3,
            "cooldown days": 2,
            "expire days": 7,
            "reward": {"Gold": 12, "Reputation": 5},
            "description": "Deliver some spare loots to Rahim."
        },
        "Lusterfield Enquiry": {
            "client": ["Lusterfolk"],
            "recipient": ["Rahim"],
            "package": [{"Letter": 1}],
            "minimum rank": 1,
            "cooldown days": 1,
            "expire days": 7,
            "reward": {"Gold": 10, "Reputation": 8},
            "description": "Deliver a letter about the village's matter to Rahim."
        },
        "The Hero's Gift": {
            "client": ["Lusterfolk"],
            "recipient": ["Lothar"],
            "package": [{"Bouquet": 1}],
            "minimum rank": 1,
            "cooldown days": 3,
            "expire days": 7,
            "reward": {"Gold": 12, "Reputation": 6},
            "description": "Deliver a bouquet from a grateful Lusterfolk to Lothar."
        },
        "Surprise Present": {
            "client": ["Sebas"],
            "recipient": ["Lothar"],
            "package": [{"Small Coffer": 1}],
            "minimum rank": 2,
            "cooldown days": 9999,
            "expire days": 7,
            "reward": {"Gold": 25, "Reputation": 5}, 
            "prerequisites": {"Quest": ["A Rolling Stone"]},   
            "description": "Deliver a Mysterious gift to Lothar after the balls incident in the shop."
            
        },
        "Shop Goods": {
            "client": ["Sebas", "Rahim"],
            "recipient": ["Lusterfolk"],
            "package": [{"Small Coffer": 1}],
            "minimum rank": 1,
            "cooldown days": 1,
            "expire days": 7,
            "reward": {"Gold": 10, "Reputation": 5},
            "description": "Deliver a special order to a Lusterfolk."
        },
        "Getting Bread": {
            "client": ["Cane"],
            "recipient": ["Ole"],
            "package": [{"Bread": 5}],
            "minimum rank": 4,
            "cooldown days": 1,
            "expire days": 7,
            "reward": {"Gold": 10, "Reputation": 6},
            "prerequisites": {"Variable": {"ole_trust_cane": True}},
            "description": "Send Ole his favourite daily meal."
        },
        "Hunter's Stew": {
            "client": ["Amble", "Jog"],
            "recipient": ["Cane"],
            "package": [{"Raw Meat": 2}, {"Sage": 2, "Reed": 2}],
            "minimum rank": 5,
            "cooldown days": 1,
            "expire days": 7,
            "reward": {"Gold": 14, "Reputation": 9},
            "prerequisites": {"Quest": ["Ole's Postal Training"]},
            "description": "Send Cane some ingredients for the Hunter's Stew."
        },
        "Royal Fabric": {
            "client": ["Sebas", "Ole"],
            "recipient": ["Rahim"],
            "package": [{"Gold": 10}, {"Hemp": 3, "Flax": 3, "Reed": 2}],
            "minimum rank": 5,
            "cooldown days": 1,
            "expire days": 7,
            "reward": {"Gold": 16, "Reputation": 10},
            "description": "Deliver Rahim the materials for making his signature fabric."
        },
        "Patching Up": {
            "client": ["Rahim"],
            "recipient": ["Arthur"],
            "package": [{"Patch": 3}, {"Strap": 2, "Loose Button": 3}],
            "minimum rank": 7,
            "cooldown days": 3,
            "expire days": 7,
            "reward": {"Gold": 20, "Reputation": 12},
            "prerequisites": {"Quest": ["Ranch Patrol"]},
            "description": "Bring sewing materials to Arthur from the farm for a scarecrow's repair."
        },
        "River Run": {
            "client": ["Lusterfolk", "Goats"],
            "recipient": ["Goats", "Lusterfolk"],
            "package": [{"Small Coffer": 5}, {"Letter": 2}],
            "minimum rank": 1,
            "cooldown days": 1,
            "expire days": 7,
            "reward": {"Gold": 18, "Reputation": 10},
            "prerequisites": {"Variable": {"goat_reconciliation": True}, "Quest": ["Reconciliation"]},
            "description": "Deliver wares and letters between the Lusterfolk and the Goats."
        },
        "Bridge Building": {
            "client": ["Amble"],
            "recipient": ["Goats"],
            "package": [{"Masonry Mix": 2, "Stone": 2}, {"Stone": 4, "Wooden Log": 4, "Wooden Bucket": 1}],
            "minimum rank": 3,
            "cooldown days": 1,
            "expire days": 7,
            "reward": {"Gold": 15, "Reputation": 12},
            "prerequisites": {"Variable": {"goat_reconciliation": True, "riverside_crossing_finished": False}, "Quest": ["Reconciliation"]},
            "description": "Deliver materials to rebuild the bridge between Lusterfield and the Goat Tribe."
        },
        "Equip for Combat": {
            "client": ["Lusterfolk"],
            "recipient": ["Kari"],
            "package": [{"Tribal Spear": 1, "Hunting Bow": 1, "Knight Longsword": 1}],
            "minimum rank": 4,
            "cooldown days": 2,
            "expire days": 7,
            "reward": {"Gold": 24, "Reputation": 10},
            "prerequisites": {"Variable": {"goat_reconciliation": True}, "Quest": ["Reconciliation"]},
            "description": "Deliver weapons to Kari to help his men arm up."
        },
        "Chief's Remedy": {
            "client": ["Ole"],
            "recipient": ["Furkan"],
            "package": [{"Green Ointment": 1}, {"Ginger": 3, "Rosemary": 4}],
            "minimum rank": 1,
            "cooldown days": 3,
            "expire days": 7,
            "reward": {"Gold": 20, "Reputation": 12},
            "prerequisites": {"Variable": {"goat_reconciliation": True}, "Quest": ["Reconciliation", "Mayor of Lusterfield"]},
            "description": "Deliver a remedy to Furkan to help him recover from the encounter in the temple."
        },
        "Rock Appraisal": {
            "client": ["Sebas"],
            "recipient": ["Gwyddyon"],
            "package": [{"Stone": 4}],
            "minimum rank": 5,
            "cooldown days": 2,
            "expire days": 7,
            "reward": {"Gold": 22, "Reputation": 8},
            "prerequisites": {"Variable": {"goat_reconciliation": True}, "Quest": ["Reconciliation"]},
            "description": "Help Sebas deliver some special stones to Gwyddyon for appraisal."
        }

    }

    rank_up_rewards = {
        2: {"Gold": 15, "Experience": 20},
        3: {"Gold": 20, "Experience": 25, "Level Up Point": 1},
        4: {"Gold": 25, "Experience": 30},
        5: {"Gold": 30, "Experience": 35, "New Job Slot": 1},
        6: {"Gold": 35, "Experience": 40},
        7: {"Gold": 40, "Experience": 45},
        8: {"Gold": 45, "Experience": 50, "New Trinket Slot": 1},
        9: {"Gold": 50, "Experience": 60},
        10: {"Gold": 60, "Experience": 70, "New Job Slot": 1},
        11: {"Gold": 70, "Experience": 85},
        12: {"Gold": 85, "Experience": 100, "Level Up Point": 1},
        13: {"Gold": 100, "Experience": 115},
        14: {"Gold": 115, "Experience": 130},
    }

    def add_job(job_name, job_detail, day):
        clients = job_detail.get('client', [])
        recipients = job_detail.get('recipient', [])
        
        valid_pairs = [(c, r) for c in clients for r in recipients if c != r]
        if valid_pairs:
            chosen_client, chosen_recipient = renpy.random.choice(valid_pairs)
        else:
            chosen_client = renpy.random.choice(clients) if clients else None
            chosen_recipient = renpy.random.choice(recipients) if recipients else None
        
        chosen_package = {}
        for possible_items in job_detail["package"]:
            chosen_item = renpy.random.choice(list(possible_items.keys()))
            chosen_package[chosen_item] = possible_items[chosen_item]
        
        chosen_bonus = []
        reward = dict(job_detail.get("reward", {}))
        if "Gold" in reward:
            reward["Gold"] += int(pc.rank/2)
        if job_detail.get("bonus", False):
            chosen_bonus = renpy.random.choice(job_detail['bonus'])
        return {
                "job": job_name,
                "client": chosen_client,
                "recipient": chosen_recipient,
                "package": chosen_package,
                "description": job_detail['description'],
                "reward": reward,
                "bonus": chosen_bonus,
                "cooldown days": job_detail["cooldown days"],              
                "expire days": job_detail["expire days"],
                "posted day": day,
                "prerequisites": job_detail.get("prerequisites", {}),
                "status": 0
            }

    def has_active_delivery(job_name):
        for delivery in active_deliveries:
            if delivery["job"] == job_name and delivery["status"] in [2, 3, 4]:
                return True
        return False

    def remove_duplicate_delivery_tasks(job_name = None, keep_task = None):
        seen_jobs = set()
        for task_list in [activetasks, completedtasks]:
            for task in task_list[:]:
                if task == None or not hasattr(task, "delivery") or task.delivery == None:
                    continue
                task_job_name = task.delivery.get("job", None)
                if task_job_name == None:
                    continue
                if job_name != None and task_job_name != job_name:
                    continue
                if task == keep_task:
                    seen_jobs.add(task_job_name)
                    continue
                if task_job_name in seen_jobs:
                    task_list.remove(task)
                else:
                    seen_jobs.add(task_job_name)

    def update_delivery_task(task, job, outcome = None):
        task.title = _(job["job"])
        task.location = _("Lusterfield")
        task.questgiver = _(job["client"])
        task.description = _(job["description"])
        task.reward = format_job_reward(job)
        task.delivery = job
        task.progress = []
        task.tProgress(format_job_description(job))
        if outcome == "failed":
            task.tProgress(_("This delivery failed. No reward was paid."))
        elif outcome == "expired":
            task.tProgress(_("This courier posting expired. No reward was paid."))
        task.completedtimes = get_task_completion_time(job["job"])

    def refresh_jobs(board, in_cooldown_jobs, day = 0, max_slots = 3, refresh_inactive_job = False):
        cancel_unavailable_jobs(board, day)
        
        if refresh_inactive_job:
            board[:] = [job for job in board if job.get("status") != 0]
        
        kept_jobs = []
        for job in board:
            if job.get("status", 0) == 0 and day > job["posted day"] + job["expire days"]:
                expire_job(job)
            else:
                kept_jobs.append(job)
        board[:] = kept_jobs
        empty_slots = max_slots - len(board)
        if empty_slots <= 0:
            return board
        available_jobs = []
        on_board_jobs = [job["job"] for job in board] 
        
        for job_name, job_detail in courier_jobs.items():
            if job_name in on_board_jobs or has_active_delivery(job_name):
                continue
            
            if job_detail["minimum rank"] > pc.rank:
                continue
            
            if job_detail.get("prerequisites", {}) != {}:
                if not checkprerequisites(job_detail):
                    continue
            
            if job_name in in_cooldown_jobs:
                if day < in_cooldown_jobs[job_name]:
                    continue
                else:
                    in_cooldown_jobs.pop(job_name)
            
            if any(not courier_character_available(client) for client in job_detail.get("client", [])):
                continue
            if any(not courier_character_available(recipient) for recipient in job_detail.get("recipient", [])):
                continue
            
            available_jobs.append(job_name)
        
        chosen_job_names = renpy.random.sample(available_jobs, min(len(available_jobs), empty_slots))
        
        for job_name in chosen_job_names:
            job_detail = courier_jobs[job_name]
            new_job = add_job(job_name, job_detail, timenow.day)
            board.append(new_job)
        
        return board

    def courier_character_available(name):
        if name == "Lothar" and lothar_hunting:
            return False
        return True

    def cancel_unavailable_jobs(board, day):
        for job in board[:]:
            if courier_character_available(job["client"]) and courier_character_available(job["recipient"]):
                continue
            
            if job.get("status") in (2, 3):
                task = look_for_delivery_task(job["job"])
                if task:
                    TaskFinish(task)
                fail_job(job, day)
                if job in active_deliveries:
                    active_deliveries.remove(job)
            
            elif job.get("status") == 4:
                continue
            
            board.remove(job)

    def format_job_description(job):
        package_items = ""
        for item, number in job["package"].items():
            package_items += "   - " + _(item)
            package_items += " x"
            package_items += str(number)
            package_items += "\n"
        
        return _("Deliver the following goods from {client} to {recipient}.\n{items}").format(
            client=_(job["client"]),
            recipient=_(job["recipient"]),
            items=package_items
        )

    def format_job_reward(job, on_board = False):
        reward_items = ""
        if on_board:
            return ", ".join("{} {}".format(v, _(k)) for k, v in job["reward"].items())
        else:
            for item, number in job["reward"].items():
                reward_items += "   - " 
                reward_items += _(item)
                reward_items += " x"
                reward_items += str(number)
                reward_items += "\n"
            return reward_items

    def begin_job(job, day):
        if job.get("status") != 0 or has_active_delivery(job["job"]):
            return
        job["start day"] = day
        job["status"] = 2
        if job not in active_deliveries:
            active_deliveries.append(job)
        new_task = look_for_delivery_task(job["job"])
        if new_task == None:
            new_task = Task(_(job["job"]), _("Lusterfield"), _(job["client"]), _(job["description"]), 1, format_job_reward(job), delivery = job)
        update_delivery_task(new_task, job)
        remove_duplicate_delivery_tasks(job["job"], new_task)
        TaskBegin(new_task)

    def finish_job(board, job, day):
        if job["job"] not in courier_stats:
            courier_stats[job["job"]] = {
                "completed": 1, 
                "failed": 0,
                "expired": 0,
                "last completed day": day,
                "last failed day": 0
                }
        else:
            courier_stats[job["job"]]["completed"] += 1
            courier_stats[job["job"]]["last completed day"] = day
        if job in board:
            board.remove(job)
        add_reward(job)
        if job in active_deliveries:
            active_deliveries.remove(job)
        task = look_for_delivery_task(job["job"])
        remove_duplicate_delivery_tasks(job["job"], task)
        TaskFinish(task)

    def fail_job(job, day):
        if job["job"] not in courier_stats:
            courier_stats[job["job"]] = {
                "completed": 0,
                "failed": 1,
                "expired": 0,
                "last completed day": 0,
                "last failed day": day
            }
        else:
            courier_stats[job["job"]]["failed"] += 1
            courier_stats[job["job"]]["last failed day"] = day
        if job in courier_board:
            courier_board.remove(job)
        if job in active_deliveries:
            active_deliveries.remove(job)
        job["status"] = 5
        task = look_for_delivery_task(job["job"])
        if task == None:
            task = Task(_(job["job"]), _("Lusterfield"), _(job["client"]), _(job["description"]), 1, format_job_reward(job), delivery = job)
        update_delivery_task(task, job, "failed")
        remove_duplicate_delivery_tasks(job["job"], task)
        if task in activetasks:
            activetasks.remove(task)
        if task not in completedtasks:
            completedtasks.append(task)
        task.taskEnd()
        task.completed_date = day
        task.completed_hour = timenow.hour

    def expire_job(job, day = None):
        if day == None:
            day = timenow.day
        if job["job"] not in courier_stats:
            courier_stats[job["job"]] = {
                "completed": 0,
                "failed": 0,
                "expired": 1,
                "last completed day": 0,
                "last failed day": 0
            }
        else:
            courier_stats[job["job"]]["expired"] += 1
        if job in courier_board:
            courier_board.remove(job)
        if job in active_deliveries:
            active_deliveries.remove(job)
        job["status"] = 6
        task = look_for_delivery_task(job["job"])
        if task == None:
            task = Task(_(job["job"]), _("Lusterfield"), _(job["client"]), _(job["description"]), 1, format_job_reward(job), delivery = job)
        update_delivery_task(task, job, "expired")
        remove_duplicate_delivery_tasks(job["job"], task)
        if task in activetasks:
            activetasks.remove(task)
        if task not in completedtasks:
            completedtasks.append(task)
        task.taskEnd()
        task.completed_date = day
        task.completed_hour = timenow.hour

    def add_reward(job):
        for reward, number in job["reward"].items():
            if reward == "Gold":
                pc.gold += number
            elif reward == "Reputation":
                pc.add_rep(number)
            else:
                addItem(reward, inventory, number)

    def sumOfValues(dictionary):
        return sum(x == True for x in dictionary.values())

    def is_client(name):
        for delivery in active_deliveries:
            if delivery["client"] == name and delivery["status"] == 2:
                return True
        return False

    def is_recipient(name):
        for delivery in active_deliveries:
            if delivery["recipient"] == name and delivery["status"] == 3:
                for item, number in delivery["package"].items():
                    if item == "Gold":
                        if pc.gold < number:
                            return False
                    elif LookForItemNumber(item, inventory) < number:
                        return False
                return True
        return False

    def client_delivery(name):
        for delivery in active_deliveries:
            if delivery["client"] == name and delivery["status"] == 2:
                return delivery

    def recipient_delivery(name):
        for delivery in active_deliveries:
            if delivery["recipient"] == name and delivery["status"] == 3:
                return delivery

    def look_for_delivery_task(job_name):
        for task in activetasks:
            if task != None and hasattr(task, "delivery") and task.delivery != None and task.delivery.get("job", None) == job_name:
                return task
        for task in completedtasks:
            if task != None and hasattr(task, "delivery") and task.delivery != None and task.delivery.get("job", None) == job_name:
                return task
        return None

    def checkprerequisites(job):
        prerequisites = job.get("prerequisites", {})
        
        quests = prerequisites.get("Quest", [])
        for quest in quests:
            if not any(completed_quest.title == quest for completed_quest in completedquests):
                return False
        
        variables = prerequisites.get("Variable", {})
        for var_name, expected_value in variables.items():
            actual_value = getattr(renpy.store, var_name, None)
            if actual_value != expected_value:
                return False
        
        return True

    def addPackage(packages, inventory):
        for item, number in packages.items():
            global reacher
            reacher = item
            if item == "Gold":
                
                pc.gold += number
            else:
                addItem(item, inventory, number)

    def removePackage(packages, inventory):
        for item, number in packages.items():
            if item == "Gold":
                pc.gold -= number
            else:
                removeItem(item, inventory, number)

    def get_task_completion_time(job_name):
        return courier_stats.get(job_name, {}).get("completed", 0)

    def get_next_rank_tooltip(current_rank):
        
        next_rank = current_rank + 1
        
        
        reward = rank_up_rewards.get(next_rank)
        
        
        if not reward:
            return _("Max Rank Reached")
        
        
        info = _("Next Rewards:\n")
        
        if next_rank % 2 == 0:
            info += _("- +1 Task Gold Reward\n")
        
        if "Gold" in reward:
            info += _("- {} Gold\n").format(reward["Gold"])
        
        if "Experience" in reward:
            info += _("- {} Experience\n").format(reward["Experience"])
        
        if "New Job Slot" in reward:
            info += _("- {} New Job Slot\n").format(reward["New Job Slot"])
        
        if "New Trinket Slot" in reward:
            info += _("- {} New Trinket Slot\n").format(reward["New Trinket Slot"])
        
        if "Level Up Point" in reward:
            info += _("- {} Level Up Point\n").format(reward["Level Up Point"])
        return info.strip()

screen courier_board_screen():
    add "#000c"
    frame:

        xalign 0.5 yalign 0.5
        xmaximum 1200
        padding (150, 150)
        background Frame("iron_frame", 0, 0)
        has vbox
        xalign 0.5 yalign 0.5
        hbox:
            ymaximum 25
            xalign 0.5 yalign 0.5
            spacing 10
            text _("Courier Rank: [pc.rank]") font "leafy.otf" size 30 color "#f3d1af" yalign 0.4
            button:
                background None
                action NullAction()
                tooltip _("Reward")
                bar:
                    value AnimatedValue(pc.rep, pc.get_next_rep_req(), 1)
                    left_bar Frame("left_yellow", 6, 6)
                    xmaximum 300

            text "[pc.rep] / [pc.get_next_rep_req()]" font "leafy.otf" size 20 color "#faecdeaa" xalign 0.35 yalign 0.35
        if len(courier_board) > 0:
            viewport:
                ysize 500
                scrollbars "vertical"
                mousewheel True
                spacing 10

                has vbox
                yalign 0.45
                spacing 30

                xfill True



                for job in courier_board:


                    $ job_client = _(job["client"])
                    $ job_recipient = _(job["recipient"])
                    $ job_reward = format_job_reward(job, True)
                    $ job_description = _(job["description"])
                    $ job_status = job["status"]

                    frame:

                        xfill True
                        padding (60, 30)
                        background Frame("paperframe", 0, 5)

                        has hbox

                        xfill True
                        spacing 10

                        for package, number in job["package"].items():
                            frame:
                                style "slot"
                                imagebutton:
                                    idle package.lower()
                                    style "click_button"
                                    unhovered SetVariable("selected_mapitem", None)
                                    action SetVariable("selected_mapitem", package)
                                if isinstance(fyi(package), Consumable) or isinstance(fyi(package), Material) or package == "Gold":
                                    text "[number]" style "invnumber_label"
                        vbox:
                            text "[job_description]" size 22 font "kingthing.ttf" bold True color "#2c221e" xmaximum 400
                            text _("From: [job_client] -> To: [job_recipient]") font "kingthing.ttf" size 20 color "#805f55"
                            text _("Reward: [job_reward]") size 20 font "kingthing.ttf" color "#ad7638"

                        vbox:
                            xalign 1.0
                            yalign 0.5
                            if job["status"] == 0:
                                frame:
                                    style "coolframe"
                                    padding (15, 10)
                                    textbutton _("ACCEPT") text_font "leafy.otf" action Function(begin_job, job, timenow.day)
                            elif job["status"] == 2:
                                frame:
                                    style "coolframe"
                                    padding (20, 15)
                                    text _("ACCEPTED") font "leafy.otf"
                            elif job["status"] == 3:
                                frame:
                                    style "coolframe"
                                    padding (20, 15)
                                    text _("DELIVERING") font "leafy.otf"
                            elif job["status"] == 4:
                                frame:
                                    style "coolframe"
                                    padding (15, 10)
                                    textbutton _("FINISH") text_font "leafy.otf" action Function(finish_job, courier_board, job, timenow.day)
        else:
            fixed:
                xfill True
                ysize 500
                text _("Come back tomorrow!\n- Postmaster") font "garamond.ttf" xalign 0.5 yalign 0.5 textalign 0.5


        frame:
            padding (15, 10)
            xalign 0.5
            style "coolframe"
            textbutton _("Leave") text_font "leafy.otf" action Return("Leave")
    frame:
        style "coolframe"
        xalign 0.5
        yalign 0.05
        xpadding 50
        ypadding 10
        text _("Courier Board") xalign 1 style_prefix "screen_title"

    if GetTooltip():
        nearrect:
            focus "tooltip"
            prefer_top True
            has frame
            style "coolframe"
            padding (20, 15)
            text get_next_rank_tooltip(pc.rank) size 25 font "leafy.otf"

label Lusterfield_Courier_Board:
    $ cancel_unavailable_jobs(courier_board, timenow.day)
    if timenow.day > last_courier_refresh_day:
        $ last_courier_refresh_day = timenow.day
        $ courier_board = refresh_jobs(courier_board, in_cooldown_jobs, timenow.day, pc.max_jobs)



    call screen courier_board_screen()

    jump main_lusterfield02

label Courier_Pickup_Dialogues:
    $ delivery = client_delivery(client_name)
    $ delivery_name = delivery["job"]
    if client_name == "Sebas":
        e "Hey, Sebas. You've got something for me to send?"
        if delivery_name == "Surprise Present":
            s "Yes! well. I didn't expect you to be the courier today."
            s "But anyway, I have this small coffer here that I need you to deliver to Lothar."
            e "Uh... what's it for?"
            if sebas_kick:
                s "N-nothing! I mean, uhm... it's Ole's ointment since I kicked him in the nuts the other day."
            else:
                s "N-nothing! I mean, uhm... he dropped this in the shop the day we went to check on that moss fellow."
            "You furrow your brows, suspiciously taking the coffer from his hands."
            e "It doesn't feel too heavy."
            s "Yeah it's for protection. Just don't open it yourself before giving it to Lothar, it's for his eyes only-"
            e "O-okay."
        elif delivery_name == "Shop Goods":
            s "Yes! A customer bought something a while back. I'm sending it to him."
            e "Oh? What is it?"
            s "Just some supplies he needed. Nothing too special."
            e "Alright, I'm on my way."
        elif delivery_name == "Settling the Debt":

            s "Roomie! You're taking my package today? Well, here's the gold I owed Cane."
            s "It's a long story, though I can't really recall what I did with it. I was really drunk, you know."
            e "Yeah I get it, Seb."
            s "Anyway, just make sure it gets to the right place, alright? I don't want him knocking on the door here."

        elif delivery_name == "Royal Fabric":
            s "Yes, yes. I've picked some flowers from the last little trip. Rahim is gonna love these."
            e "Oh? What are they for?"
            s "His special kind of fabric, you know how it is. That old bull likes turning these flowers into something nice and smooth."
            e "Alright then, I'll get these to him in a moment."
        elif delivery_name == "Rock Appraisal":
            s "Oh, yes. Take these, take these to Gwyd, roomie."
            e "W-what are those, stones?"
            s "Stones, Rocks. I picked them up on the road the other day, looking odd aren't they, I'm thinking they're no ordinary rocks."
            e "Well then, what are they?"
            s "I don't know, that's why I need Gwyd to appraise them for me, it's gotta be gold this time."
            e "A-alright, Seb. I'll let him look at the rocks."

    elif client_name == "Ole":
        e "Hey, Ole. You've got something for me to send?"
        if delivery_name == "Tending New Wounds":

            o "Yeah. Well, I just need you to take this Ointment, the boys out there got themselves hurt again."
            o "Make sure to give it to them quickly, [e]. We're counting on you."
            e "Oh, no problem!"
        elif delivery_name == "Royal Fabric":
            o "Rahim's flowers. He specifically asked for those the last time we met."
            e "Oh? And the gold too?"
            o "Yes, it's the gold lining. It's important for the fabric, as he said so."
            e "Alright then, I'll get these to him in a moment."

        elif delivery_name == "Chief's Remedy":
            o "It's for the goat chief. Make sure you get this to him quickly kiddo."
            o "I've heard Furkan's been really out of it since that incident in the temple, this might help him with the pain."
            e "Okay, I'll make sure all of this gets to him safely."

    elif client_name == "Cane":
        e "Cane, you need to send something?"
        c "Aye, I baked a few too many breads today, take those to Ole would'ya?"
        c "Heard he likes them wheaty grubs. Ol' lizard's rounding out his belly proper."
        e "Alright, I'll be on my way."

    elif client_name == "Lothar":
        e "Lothar, do you need something to send?"
        l "Yes, disciple. I came back from another successful adventure, and there are some spare loots for the old bull."
        l "Make sure that old bull gets his cloths, disciple. Maybe one day, one day I'll take you to my next adventure."

    elif client_name == "Rahim":
        e "Hey, Rahim. You've got something for me to send?"
        if delivery_name == "Shop Goods":

            r "Yes, I need you to take the order to the Lusterfolk. It's right over there."
            e "What's it?"
            "The bull look up from his table, his eyes narrowing."
            r "A garment, body covering."
            "Rahim turns back as his hand pushes you towards the door."
        elif delivery_name == "Patching Up":
            r "Here they are. Just some spare parts I had lying around."
            r "The dog over at the farm moaned about the scarecrow again."
            e "Oh? The scarecrow? What happened to it?"
            r "Landshark's bites... or someone ticked him off most probably."
            e "A-alright. I am on my way."

    elif client_name == "Lusterfolk":
        e "Hey, Haimo, do the folks need anything sent?"
        if delivery_name == "Lusterfield Enquiry":
            hm "Yes, one, actually. I need you to take this letter to Rahim."
            hm "Looks to be some sort of inquiry about the city's matter."
            if renpy.random.random() > 0.5 and quest37.status == False and not haimo_dialogue["Questions"].get("Rahim Mayor", False):
                menu:
                    "Ask about Mayor":
                        $ haimo_dialogue["Questions"]["Rahim Mayor"] = True
                        e "Oh? Why did he send it to Rahim?"
                        hm "We're used to Rahim being the go-to guy for these matters, not sure why."
                        hm "As you probably know, we don't have a mayor around here, so he's probably the closest we have since the incident with the goats."
                        e "Why not just make him the Mayor, then?"
                        hm "I don't know, I've heard stories from the elders that we don't talk about the last mayor anymore, they said after he died, all the candidates just... mysteriously died, in different ways."
                        hm "So, we just never had a leader since then, until the goats attacked."
                        e "I see."
                    "I'll get into it.":
                        pass
            e "Alright, I'll take it to Rahim then."
            hm "Don't take too long, Rahim's waiting."
        elif delivery_name == "The Hero's Gift":

            hm "Yes. I have a bouquet here, for Lothar they said."
            hm "Looks like an admirer of his. There's been dozens of these every week."
            hm "I think he tosses it aside after getting them, it's a shame, look at all those special flowers."
            if renpy.random.random() > 0.5 and not haimo_dialogue["Questions"].get("Drowned Sage", False):
                menu:
                    "Ask about the flowers":
                        $ haimo_dialogue["Questions"]["Drowned Sage"] = True
                        e "What about the flowers?"
                        hm "Oh, you see, this, this blue one. They called it the drowned sage. It was said that when Lusterfield flooded, it was one of the few plants that stood tall."
                        hm "It was the first thing the settlers saw when the waters receded, and it was glistening blue, they said it was the last blessing of the forest god."
                        e "This flower... it has quite the story."
                        hm "Yeah, it does. It's only seen in Lusterfield, and there weren't many left today."
                        hm "Well, if I keep talking I'm afraid the flowers are going to wilt. Get them delivered instead, won't you?"
                    "I get it":
                        pass
            e "Alright, I'll take it to Lothar then."
            hm "Good. And be gentle with the flowers."
        elif delivery_name == "River Run":
            hm "Just a few coffers and letters here and there I need you to take to the Goats."
            hm "The Goats are still pretty touchy with us, so just drop them in the community box and they'll have goats take care of it."
            e "Alright, I'll get them to the goats now."
            hm "On your way then."

        elif delivery_name == "Equip for Combat":
            hm "It's a weapon, commissioned from the goats for one of their huntsmen. Take those to the general and he'll know what to do."
            hm "Be careful and try not to prick your innards on the way there."
            "Haimo chuckles to himself as he hands you the weapon."
            if renpy.random.random() > 0.5 and not haimo_dialogue["Questions"].get("Kari", False):
                hm "Oh, have you met the general? Kari? I saw him around asking about the courier board a few times."
                e "I did. A few times."
                hm "He's got that mask... I happened to read about it earlier, it was quite interesting where the tradition came from."
                menu:
                    "Ask about the mask":
                        $ haimo_dialogue["Questions"]["Kari"] = True
                        e "What about the mask?"
                        hm "They said a long long time ago, one night, every goat saw the drifter in their dream."
                        e "W-wait, who's the drifter?"
                        hm "A mysterious deer with a cane on his hand, his face is obscured I think."
                        hm "Anyway, they said the drifter was someone connected to the gods, so in order to communicate with the drifter, they had a deer dressing up like him to act as their shaman."
                        hm "A mask, a staff, some antlers, with a hint of artistic liberty of course, that was how it all started."
                        hm "They never saw the drifter again, and they had not have a summoning ritual for a while now, but the tradition stuck around til now."
                        e "That's... odd. I've heard something from Kari but not to that extent."
                        hm "It's a strange story isn't it? I'm sure the general himself would be happy to tell you about it if you ask him."
                        e "Um, I'm not sure he's ever happy at anything, but thanks."
                    "I get it":
                        pass
            e "Alright then, I'll give it to Kari."
            hm "Good, take care!"


    elif client_name == "Amble":
        e "Hey, Amble. Do you have something for me?"
        if delivery_name == "Bridge Building":
            a "Here, here. I need you to take those to the goats, for their bridge building project."
            e "Oh? Those are a lot of heavy stuff!"
            a "Yes, after the vote I kept thinking about the bridge, I've gathered the materials, but it's difficult to build it all by myself."
            a "The goats can make use of it, I've talked to their chief about it, he sounded rather keen."
            e "Alright, if it isn't the chief himself! I'll take those to their tribe then."
            a "Thanks, [e]!"

        elif delivery_name == "Hunter's Stew":

            a "Yes, I've collected a bit of meat scraps today for Cane."
            a "Here it is, the stew's going to taste amazing."
            "You take the scraps from Amble."
            e "Alright, I'll take it to Cane then."
            a "Thanks! Puny courier."

    elif client_name == "Jog":
        e "Jog, I've heard you needed to send something?"
        j "Oh, yeah. Just some meat and stuff. Here you go."
        j "I'd have gone myself but I'm not entirely in the mood for it."
        "Jog yawns as he slouches on the hay bales. Hands behind the back of his ears, he lazily tosses the ingredients to you."
        e "Alright, I'll hand it to Cane then."

    elif client_name == "Goats":
        e "Officer, is there anything you need to send over the river?"
        gof "Yes, this one,"

    $ addPackage(delivery["package"], inventory)
    $ delivery["status"] = 3

    return

label Courier_Delivery_Dialogues:
    $ delivery = recipient_delivery(recipient_name)
    $ delivery_name = delivery["job"]
    if recipient_name == "Rahim":
        e "Rahim, I've got a delivery for you."
        r "Which one is it?"
        if delivery_name == "Shop Goods":
            e "It's a letter, addressed to you."
            if quest37.status == False:
                r "Ugh, alright. Just leave it on the pile over here."
                "He points towards the corner of the room, where a stack of letters and packages is piled high."
                e "Uhm, do you even read them?"
                r "I'll read it when I have time. If it's really urgent they'll come find me."
                "He shrugs."
            else:
                r "Alright, give it to me."
                "You hand over the letter to Rahim, but he looks a bit peeved."
                e "Is everything alright?"
                r "Yeah, just another headache to go through, thanks for the letter though."

        elif delivery_name == "Adventure Discovery":

            e "It's from Lothar, he said you might need some spare loots from him."
            r "Ugh, fine. Just leave it on the table. Thanks."
            "Rahim returns to his workbench, grumbling as you put down the clothes."

        elif delivery_name == "Royal Fabric":
            e "It's the flowers and gold, seems like Sebas and Ole collected them for you."
            r "Finally, those took long enough. I'll get to work on the outfit right away."
            "Rahim takes the flowers and gold from you, his eyes lighting up."
            r "These are perfect, just what I needed. Thanks, [e]."

    elif recipient_name == "Ole":
        e "Ole, I've got a delivery for you."
        o "Oh? Kiddo, you didn't-"
        "Ole's eyes light up as soon as he sees the few pieces of bread in your hands."
        e "It's a few pieces of bread, Cane said you liked them."
        o "Yes! I can smell that tavern hearth's aroma from miles away. Thank you, [e]."

    elif recipient_name == "Cane":
        if delivery_name == "Settling the Debt":
            e "Hey, Cane. I've got a delivery for you. It's from Sebas."
            c "Oh, the gold he owed me for?"
            e "Yeah, here it is."
            c "Lemme see, lemme see..."
            c "Yeah, lad, that's the one. Thanks, and tell'm to maybe stop playing bets in my place, will ya?"
            "You nod."
        elif delivery_name == "Hunter's Stew":
            e "Cane, I've got a delivery for you. It's some meat, and a few pieces of flower."
            c "Ooh! Great! Put'em into the stew here would'cha?"
            "You turn to the pot and add the ingredients one by one. Cane stirs the pot with a ladle, the aroma of the meat instantly fills the air."
            c "Thanks lad. Got a good feeling about this one, come by in a moment and I'll get ya a taste."
            e "Haha, looking forward to it."

    elif recipient_name == "Lothar":
        e "Hey, Lothar. I've got a delivery for you."
        if delivery_name == "Tending New Wounds":
            e "It's from Ole."
            l "Nice... where's it?"
            e "Right here."
            "You hand over the ointment to Lothar."
            l "Just what I needed. I tell you, [e]. This is the only reason why I stayed cordial with that lizard."
            e "Glad to hear it."
            l "You can go now, disciple."
        elif delivery_name == "The Hero's Gift":
            l "First, call me Lothar. Second, a gift? From who?"
            "You hand over the bouquet to Lothar."
            e "It's from an admirer of yours. It said you saved their life recently."
            "You notice a faint frown on Lothar's face as he stares at you."
            l "I see..."
            l "Huh... I wonder who it could be, I've saved so many of them lately."
            l "Maybe I should start keeping a list. Did I save more this week?"
            l "You may go now, disciple. Also, maybe you can learn a thing or two from this... admirer."
        elif delivery_name == "Surprise Present":
            l "Oh? What's this? I don't remember getting something like this."
            l "Who sent it?"
            e "Uh, Sebas."
            l "That lion, what's he got for me? An apology for the humiliation I suffered that day?"

            menu:
                "Lothar takes the coffer from you, inspecting it closely."
                "Open it yourself":
                    e "Well, let me first check what's inside."
                    l "W-what are you doing, disciple."
                    "You yank the coffer from Lothar hands, opening it yourself."
                    "As soon as you open it, a ball of gust bursts out, it doesn't smell too appetizing."
                    e "Owww-"
                    "You stumble back, rubbing your snout, Lothar quickly catches you."
                    l "The fuck was that?"
                    e "I have no idea... Sebas told me to give it to you personally."
                    l "Fucking lion, I won't be forgetting this. Let him know."
                "Wait":
                    "As soon as Lothar flips open the lid, a ball of gust bursts out, it doesn't smell too appetizing."
                    l "What the f- Ugh-"
                    "You can't help but laugh at the sight, as Lothar's expression shifts from surprise to disgust."
                    l "Disciple, are you trying to kill me?"
                    e "No, no. I- I don't know anything about this."
                    l "You better not be lying to me, I can smell your lies, [e]."
                    "You gulp."
                    l "And that lion... I won't be forgetting this. Let him know."
            "Lothar looks away as his expression softens."
            l "Now go. I need to clean after this."

    elif recipient_name == "Jog":
        e "Hey, Jog. I've got a delivery for you. It's from Ole."
        j "Oh, good. Just throw the thing over here. My body's aching like hell."
        "You toss the ointment over to Jog. He quickly opens it and smears it over his fur."
        j "Ahh, that's much better. Thanks, [e]."
        e "No problem, Jog. Just take it easy, alright?"
        "He gives you a light chuckle."

    elif recipient_name == "Kari":
        if delivery_name == "Equip for Combat":
            e "Kari, I've got a delivery for you. It's from Lusterfield."
            k "What's this...?"
            "Kari grabs the weapon from your hand, he inspects it closely, tapping it against his palm a few times."
            k "Uh huh, it's... adequate. For what it's worth, my men will like the quality quite a bit."
            k "Give my gratitude to your weaponsmith."
            e "Will do!"

    elif recipient_name == "Furkan":
        if delivery_name == "Chief's Remedy":
            e "Furkan, here's some supplies I've got from Ole."
            f "Thank you, courier. It will help with the pain."
            e "A-are you alright, Furkan? Does it still hurt?"
            f "Yes, it has been better since that day, after all. But the pain still somewhat lingers."
            e "Fair enough, take care Furkan."
            "The goat chief nods."

    elif recipient_name == "Gwyddyon":
        if delivery_name == "Rock Appraisal":
            e "Gwyddyon, Sebas said he wants you to appraise these stones."
            g "Again? How many useless rocks is he gonna send my way..."
            "Gwyddyon points to the shelf full of rocks behind him, all in different shapes and sizes."
            g "Put them over these, please."
            e "Um, are you gonna appraise them?"
            g "Yes, my appraisal is... no don't let him know. I'll keep the stones safe. Just tell him to bring different rocks next time."
            e "A-alright. Will do."

    elif recipient_name == "Arthur":
        if delivery_name == "Patching Up":
            e "Rahim sent here some spare parts for the scarecrows."
            ar "Oh, good. That damn thing keeps getting his insides eaten by those landsharks."
            e "Are they alright?"
            ar "Don't you worry, little pup. They don't die, or they don't get to."

    elif recipient_name == "Lusterfolk":
        e "Haimo, here's a coffer for you."
        hm "You mean, for the Lusterfolk, huh? Right, I'll make sure it gets to them. Thanks."

    elif recipient_name == "Goats":
        e "Officer, here's some stuff from Lusterfield."
        gof "What is it? Take it closer..."
        "You wait as the officer squints, leaning forward more and more."
        gof "Oh yes, it's for the goats, right."
        gof "Well, thanks, boy. I'll take it from here."

    $ unlock_day = timenow.day + delivery['cooldown days']
    $ in_cooldown_jobs[delivery["job"]] = unlock_day
    $ removePackage(delivery["package"], inventory)
    $ delivery["status"] = 4
    return

label Haimo_Dialogue:
    hide screen menu_buttons
    show haimo_idle
    $ haimo_dialogue["Encounter"] += 1
    if haimo_dialogue["Encounter"] == 1:
        "You walk up towards the courier board, where a hefty goat stands, leaning against the tree lazily."
        hm "Just put what you need to send right over there. Make sure the name of the recipient is legible."
        "The goat watches you with a bored expression. His words almost slurred together as he speaks."
        e "Hey... Haimo? You're the Postmaster, right? Ole asked me to talk to you."
        hm "Hmmm, what does he want?"
        "You show him the courier badge on your bag. He raises an eyebrow, intrigued."
        hm "Oh, I see. You're the new courier, huh? Nice to meet you, young man. The courier board is over there."
        e "My name is [e]. And nice to meet you, Haimo."
        "The postmaster's eyes brightens as he leans in closer to inspect you."
        hm "Doesn't look too bad. The other couriers would have you go through more trainings, but clearly Ole has faith on you."
        hm "Just make sure to follow the procedures, alright?"
        "You nod in agreement."
        hm "Good. Here's a few things you need to know before I let you go on your first delivery."
        hm "First, you can't steal anything from the packages. If you do, you're out of the job."
        hm "Second, always double-check the recipient's name and address before leaving."
        hm "And last but not least, don't lose your badge. It's your lifeline out there."
        e "Oh, I see. Is there anything else I should know?"
        hm "Well, don't miss a delivery, you'll be penalized."
        e "By who?"
        menu:
            hm "By me, of course. Some deliveries expire after a certain time, so make sure you get them done on time."
            "What if I have questions later?":
                e "What if I have questions later?"
                hm "You can always come back to me. Ask me anything, if you'd like."
            "What if I need help with a delivery?":
                e "What if I need help with a delivery?"
                hm "Just ask around. There are plenty of folks around here who can lend a hand."
            "Got it":
                pass
        e "Got it."
        hm "Good. Now get out there and make those deliveries."
        jump main_lusterfield02
    else:
        e "Good day, Haimo."
        hm "Good day, [e]."

    jump Haimo_Normal_Talk

label Haimo_Normal_Talk:

    menu:
        hm "Got any packages to send today?"
        "Pick up delivery from Lusterfolks" if is_client("Lusterfolk"):
            $ client_name = "Lusterfolk"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_2
        "Deliver goods to Lusterfolks" if is_recipient("Lusterfolk"):
            $ recipient_name = "Lusterfolk"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_2
        "Ask about the Postmaster":
            menu:
                "Ask about him as a goat":
                    $ haimo_dialogue["Questions"]["Goat"] = True
                    e "So, Haimo... you're a goat, huh?"
                    hm "That's right. What's the matter with that?"
                    e "But why are you a goat?"
                    "The postmaster squints."
                    hm "We need to work on the wording here, [e]. It's coming off very outlandish."
                    hm "Look, courier. Lusterfield is all I've ever known, I don't have anything to do with the goats out there."
                    e "So, you were raised here?"
                    hm "Yes, I was never a part of the tribe in the west. My ancestors were one of the few goats that settled back here."
                    e "I see."
                    hm "Well, rather than digging into my heritage, did you know that us goats are excellent climbers? We could scale through the mountains like it's nothing."
                    hm "The strength comes from my paws, you see, the rough pads here are tough and rubbery, it's like suction cups on each of my finger gripping into a hard surface."
                    "Haimo presents you with his paws, he clutches the surface of the tree tightly, his feet firmly balances on the rough bark of the tree."
                    hm "It works on any surface, honestly. I wouldn't let go even if I wanted to."
                    e "I'd love to try it out one day..."
                    hm "Maybe you can give it a shot sometime."
                    "The goat shrugs."
                "Ask about the history of courier":
                    $ haimo_dialogue["Questions"]["Courier History"] = True
                    e "What's the deal with couriers?"
                    hm "Oh? Didn't know you were the inquisitive type."
                    hm "Couriers have been around for ages, as you probably know, the terrain and weather can be quite challenging, and wild creatures can pose a threat."
                    hm "That's where the couriers come in, braving the elements and dangers to ensure that important items reach their destinations safely and on time."
                    e "Sounds like a tough job."
                    hm "Did you know, couriers used to be messengers for the royalties? It's not until the giant rift that formed in the eastern mountains that we started having our own couriers."
                    hm "Now, Lusterfield has our very own couriers running on errands across the village, ensuring everything runs smoothly."
                    hm "For this side of the mountains, we used to mainly run between the village and the goat tribe across the river. They had their own wagons for transport, but we were way faster for urgent deliveries."
                    e "I see."
                    hm "Did I bore you? Well, let's change the subject before I start getting into the details that's worth 10 hours of listening."
                "Ask about the courier system":
                    $ haimo_dialogue["Questions"]["Courier System"] = True
                    e "Postmaster, what's the courier job like around here?"
                    hm "You deliver messages and packages between the villagers around here, usually. It's a vital role, the village is rather big so we have to be quick on our feet to get things where they need to go."
                    hm "Everyone has their own rank, the higher your rank, you'll get more deliveries with better rewards."
                    hm "When you meet new people around here, you can get new requests from them as well."
                    e "Alright, do I need to do anything special to rank up?"
                    hm "Just keep doing your deliveries and building your reputation. The more reliable you are, the more opportunities you'll get."
                    hm "Also, I forgot to mention, if you see Lusterfolk in your deliveries, just come ask me. We'll handle the rest."
                "Ask about his postmaster job" if sumOfValues(haimo_dialogue["Questions"]) >= 3:
                    $ haimo_dialogue["Questions"]["Postmaster"] = True
                    e "So, Haimo, how did you become the postmaster?"
                    hm "Ah, that's... well. I started as a regular courier, just like you. I became a courier and worked my way up."
                    hm "But the others, they can be quite challenging, we used to have our fair share of disagreements and compete for deliveries to earn our keep."
                    hm "As you know, we didn't have a proper mayor around here so no one was here to handle their disputes, so one day some of them came up to me and asked if I could help handle the courier board."
                    hm "I agreed, and so they called me the postmaster. I guess part of the reason why they picked me was because I was never involved in any of their squabbles."
                    e "Sounds like you're the right one for the job then."
                    hm "Well, I try my best. But I can't say if the job is not quite boring. Most of the time I'm just standing here, waiting for deliveries to come in."
                    e "I know, you do look kinda bored all the time."
                    hm "I... I do? It's just my resting face I assure you. W-well, I guess maybe, it's been a while since someone held a conversation with me for so long."
                    "The postmaster blushes as his hand scratches the back of his head, looking away awkwardly."
                    hm "Those other couriers just check the board and go, without a word. I appreciate you taking the time to chat with me, sometimes, maybe, I guess."
                "That's all":
                    jump Haimo_Normal_Talk
        "That's it for now":

            e "That's enough for now, thanks, Haimo."
            if sumOfValues(haimo_dialogue["Questions"]) >= 3:
                hm "That soon? O-Okay. I'll be here if you need anything else."
            else:
                hm "Anytime, come back if you've got more questions."
            jump main_lusterfield02
    jump Haimo_Normal_Talk

label Kechioeren_Courier_Office:
    if haimo_dialogue.get("Goat Courier Office", False) == False:
        $ haimo_dialogue["Goat Courier Office"] = {}
        "You enter the courier office in goat tribe. It seems to be abandoned for a while, with a few letters and boxes scattered around the desk at the center of the room."
        "Behind the desk it was an old goat, mostly black fur with some strips of white on his arms and a full white beard, scribbling something on a yellowed book. He raises his head, and addresses you."
        my "What can I help, [e]?"
        e "Oh! You know my name?"
        my "Yes, you are the courier goat that saved our Chief, right? We've heard your story."
        my "That kid, Furkan, someone need to look after. the deer's too prideful to listen, so it's all depends on you, boy."
        e "Uhm... yeah?"
        my "Oh, what was I writing about..."
        my "Yes, courier. You are still the courier from over the river, right?"
        e "I am, and you are?"
        gof "You don't need to remember my name, I'm just an old goat handling letters and materials from Lusterfield."
        e "O-okay, officer."
        gof "The office shut down after the, you know, but now the kid asked me to come back, oh... well, at least I've got something to spend my time with."
        gof "If you have something for the other goats, just give it to me, [e]. I will hand them out later."
        e "Got it!"
        gof "Now, is there something you need?"
    else:
        "You enter the courier office again, the officer lies back on his wooden chair, reading something that looks like a letter with squinted eyes."
        gof "Oh, you almost scared me there. What do you need, again?"

    jump Kechioeren_Officer_Dialogue

label Kechioeren_Officer_Dialogue:
    menu:
        "Pick up delivery from the goats" if is_client("Goats"):
            $ client_name = "Goats"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_3
        "Deliver goods to the goats" if is_recipient("Goats"):
            $ recipient_name = "Goats"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_3
        "That's it for now":
            e "That's enough for now, thanks, officer."
            gof "Alright, then."
            jump main_kechioeren01
    jump Kechioeren_Officer_Dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
