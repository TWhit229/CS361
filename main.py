import os
import json
import requests
# Load teams array from JSON file


def load_teams():
    response = requests.get('http://127.0.0.1:5000/teams')
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data from server. Status code: {response.status_code}")
        return []

teams = load_teams()

teams = load_teams()

def print_nfl_logo():
    logo = """
                                             .d.                                             
                                            ,XkX,                                            
                                          .O0,.'OO'                                          
                      k;               .c0k;.....;k0c.               ;k.                     
                     .MOOkl;..   ..,cxOkc...........ckOxc,..   ..;okOkM.                     
                     .M:..,coxkkkxoc;........'loxodx....;loxkkkxoc,..:M.                     
                     .M:....,.......;......oXNxdodMMd...;.......,....:M.                     
                     .M:..lONd;...lONd:..;NN0ddOKMMMO.;dNOl...;dNOl..:M.                     
                     .M:..,KOk....'KOO..'WXxddXMMMMMd..kOK'....xOK,..:M.                     
                     .M:................dMK,kXMMMMMK.................:M.                     
                     .M:...,x......,k...kW:NMMMMMWx.....x,......x,...:M.                     
                     .M:..lWMK;...lWMK:.ckKMMMW0o.....;KMWl...;KMWo..:M.                     
                     .M:..,c,l....'c,l...:doc,.........l,c,....c,c,..:M.                     
                     .M:..,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,..:M.                     
                     .M:..X0000KWMN000000N0000000000XX000000XMMMMMN..;M.                     
                     .M:..Xd,...:WNo'..'dNx'........,0l....cKMMMMMN..:M.                     
                     .M:..NMk....oMMk..;MMMc...KXXXk,lM;..'WMMMMMMN..:M.                     
                     .M:..NMk.....kMk..;MMMc...NMMMWWWM;..'WMMMMMMN..:M.                     
                     .M:..NMk.....'Kk..;MMMc...NMMK'xMM;..'WMMMMMMN..:M.                     
                     .M:..NMk..:;..;x..;MMMc...''''.dMM;..'WMNNWMMN..:M.                     
                     .M:..NMk..lK'..'..;MMMc...dxxd'dMM;..'0,..'lNN..:M.                     
                     .M:..NMk..lMk.....;MMMc...NMMM0XMM;..'k.....;N..:M.                     
                     .M:..NMk..lMMo....;MMMc...NMMMMMMM;..'WKkk:..K..:M.                     
                     .M:..Xx:..lMMWc...;MMMc...XMMMMMMM;..'WMMN,.;N..:M.                     
                      Wl..0O;..;NMMN,..;MMMc...XMMMMMMO'...odl'.;X0..cM                      
                      lX'..dNKdlkMMMK;.cMMX;...XMMMMMc.,;:::::oOXd..'Xo                      
                       ;Xd'..,lx0XWMMMWMMMOo;..OMMMMMNWMMMWX0kl;..'dX:                       
                         :kOd:'.....,;ldONMMMXdcWMMNOdc;'.....':dOk:                         
                            .:dkkkkxoc;...'lOWMWOl'...;coxkkkkdc.                            
                                   ..,lxOkc..'l'..:kOxl;..                                   
                                         .lKx'..xKl.                                          
                                            ;XxX:                                             
                                             .d.              
    """
    print(logo)

def main_menu():
    os.system('clear')  # Clears the screen before displaying the logo and menu
    print_nfl_logo()
    print("Welcome to the NFL Stat Tracker!\n")
    print("How to Use the Program:")
    print("- Login: Create an account or login as an existing user to save teams and players.")
    print("- Search Team: Search for an NFL team by name or location and optionally save them to your profile.")
    print("- Search Player: Search for players by last name and save them to your profile.")
    print("- Search News: Find NFL news articles by searching for keywords in the headlines.\n")
    print("1. Login")
    print("2. Search Team")
    print("3. Search Player")
    print("4. Search News")

    choice = input("Please enter your choice (1-4): ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice, please select a number between 1 and 4.")
        choice = input("Please enter your choice (1-4): ")
    
    if choice == '1':
        login_menu()
    elif choice == '2':
        search_team(None)
    elif choice == '3':
        search_player(None)
    elif choice == '4':
        search_news()


def login_menu():
    os.system('clear')  # Clears the screen before displaying the login menu
    print("Login Menu:")
    print("1. Login as existing user")
    print("2. Create account")
    print("3. Go back to main menu")

    choice = input("Please enter your choice (1-3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice, please select a number between 1 and 3.")
        choice = input("Please enter your choice (1-3): ")
    
    if choice == '1':
        login_existing_user()
    elif choice == '2':
        create_account()
    elif choice == '3':
        main_menu()
def reload_user_data(username):
    with open('users.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            stored_username, stored_password, saved_data = user.strip().split(', ', 2)
            if stored_username == username:
                return saved_data
    return None

def login_existing_user():
    os.system('clear')  # Clears the screen before displaying the login menu
    username = input("Enter your username: ")
    with open('users.txt', 'r') as file:
        users = file.readlines()
        user_exists = False
        for user in users:
            stored_username, stored_password, saved_data = user.strip().split(', ', 2)
            if stored_username == username:
                user_exists = True
                password = input("Enter your password: ")
                if stored_password == password:
                    print("\nLogin successful!")
                    logged_in_menu(username, saved_data)
                else:
                    print("\nIncorrect password.")
                    retry_login()
                break
        if not user_exists:
            print("\nUsername does not exist.")
            retry_login()

def retry_login():
    print("1. Go back to main menu")
    print("2. Try again")
    choice = input("Please enter your choice (1-2): ")
    while choice not in ['1', '2']:
        print("Invalid choice, please select 1 or 2.")
        choice = input("Please enter your choice (1-2): ")
    if choice == '1':
        main_menu()
    elif choice == '2':
        login_existing_user()

def create_account():
    os.system('clear')  # Clears the screen before displaying the create account menu
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    with open('users.txt', 'a') as file:
        file.write(f"\n{username}, {password}, {{\"teams\": [], \"players\": []}}")
    print("\nAccount created successfully!")
    main_menu()


def logged_in_menu(username, saved_data):
    os.system('clear')  # Clears the screen before displaying the logged-in menu
    print("Welcome back to the NFL Stat Tracker!\n")
    print("How to Use the Program:")
    print("- Search Team: Search for an NFL team by name or location and optionally save them to your profile.")
    print("- Search Player: Search for players by last name and save them to your profile.")
    print("- Search News: Find NFL news articles by searching for keywords in the headlines.")
    print("- Saved Teams and Players: View the teams and players you have saved.\n")
    print("Logged In Menu:")
    print("1. Search Team")
    print("2. Search Player")
    print("3. Search News")
    print("4. Saved Teams")
    print("5. Saved Players")
    print("6. Logout")

    choice = input("Please enter your choice (1-6): ")
    while choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice, please select a number between 1 and 6.")
        choice = input("Please enter your choice (1-6): ")
    
    if choice == '1':
        search_team(username)
    elif choice == '2':
        search_player(username)
    elif choice == '3':
        search_news()
    elif choice == '4':
        saved_teams(username, saved_data)
    elif choice == '5':
        saved_players(username, saved_data)
    elif choice == '6':
        main_menu()


def saved_teams(username, saved_data):
    os.system('clear')
    saved_data_dict = json.loads(saved_data)
    saved_teams_list = saved_data_dict.get('teams', [])
    print(f"\nSaved Teams for {username}:")
    for index, team_name in enumerate(saved_teams_list, start=1):
        for team in teams:
            if team['name'] == team_name:
                print(f"{index}. {team['name']}: {team['wins']} Wins, {team['losses']} Losses")
    
    if saved_teams_list:
        delete_choice = input("\nWould you like to delete a saved team? Enter the number or 'n' to skip: ")
        if delete_choice.isdigit() and 1 <= int(delete_choice) <= len(saved_teams_list):
            confirm_delete = input("Are you sure you want to delete this team? (y/n): ")
            if confirm_delete.lower() == 'y':
                team_to_delete = saved_teams_list[int(delete_choice) - 1]
                saved_teams_list.remove(team_to_delete)
                with open('users.txt', 'r') as file:
                    users = file.readlines()
                with open('users.txt', 'w') as file:
                    for user in users:
                        stored_username, stored_password, saved_data = user.strip().split(', ', 2)
                        if stored_username == username:
                            saved_data_dict['teams'] = saved_teams_list
                            saved_data = json.dumps(saved_data_dict)
                            file.write(f"{stored_username}, {stored_password}, {saved_data}\n")
                        else:
                            file.write(user)
                # Reload updated saved data
                saved_data = reload_user_data(username)
    
    input("\nPress Enter to return to the Logged In Menu...")
    logged_in_menu(username, saved_data)



def saved_players(username, saved_data):
    os.system('clear')
    saved_data_dict = json.loads(saved_data)
    saved_players_list = saved_data_dict.get('players', [])
    print(f"\nSaved Players for {username}:")
    for player_name in saved_players_list:
        for team in teams:
            for player in team['players']:
                full_name = f"{player['last_name']}, {player['first_name']}"
                if full_name == player_name:
                    print(f"{player['last_name']}, {player['first_name']} - {player['position']} #{player['number']} (Team: {team['name']})")
    input("\nPress Enter to return to the Menu...")
    logged_in_menu(username, saved_data)

def search_team(username):
    os.system('clear')
    search_input = input("Enter the name or location of the team you want to search for: ").lower()
    matches = []

    for team in teams:
        if search_input in team['name'].lower() or search_input in team['location'].lower():
            matches.append(team)

    if matches:
        for team in matches:
            print(f"\n{team['name']}: {team['wins']} Wins, {team['losses']} Losses")
            if username:
                save_choice = input("\nWould you like to save this team? (y/n): ")
                if save_choice.lower() == 'y':
                    with open('users.txt', 'r') as file:
                        users = file.readlines()
                    with open('users.txt', 'w') as file:
                        for user in users:
                            stored_username, stored_password, saved_data = user.strip().split(', ', 2)
                            if stored_username == username:
                                saved_data_dict = json.loads(saved_data)
                                saved_teams_list = saved_data_dict.get('teams', [])
                                if team['name'] not in saved_teams_list:
                                    saved_teams_list.append(team['name'])
                                saved_data_dict['teams'] = saved_teams_list
                                saved_data = json.dumps(saved_data_dict)
                                file.write(f"{stored_username}, {stored_password}, {saved_data}\n")
                            else:
                                file.write(user)
                    # Reload updated saved data
                    saved_data = reload_user_data(username)
    else:
        print("\nTeam not found.")
    input("\nPress Enter to return to the Logged In Menu...")
    main_menu()


def search_player(username):
    os.system('clear')
    last_name = input("Enter the last name of the player you want to search for: ").lower()
    player_list = []
    for team in teams:
        for player in team['players']:
            if last_name in player['last_name'].lower() or last_name in player['first_name'].lower():
                player_list.append((player, team['name']))
    
    if player_list:
        print(f"\nPlayers matching '{last_name}':")
        for index, (player, team_name) in enumerate(player_list, start=1):
            print(f"{index}. {player['last_name']}, {player['first_name']} - {player['position']} #{player['number']} (Team: {team_name})")
        if username:
            save_choice = input("\nWould you like to save any of these players? Enter the number or 'n' to skip: ")
            if save_choice.isdigit() and 1 <= int(save_choice) <= len(player_list):
                selected_player = player_list[int(save_choice) - 1][0]
                with open('users.txt', 'r') as file:
                    users = file.readlines()
                with open('users.txt', 'w') as file:
                    for user in users:
                        stored_username, stored_password, saved_data = user.strip().split(', ', 2)
                        if stored_username == username:
                            saved_data_dict = json.loads(saved_data)
                            saved_players_list = saved_data_dict.get('players', [])
                            player_name = f"{selected_player['last_name']}, {selected_player['first_name']}"
                            if player_name not in saved_players_list:
                                saved_players_list.append(player_name)
                            saved_data_dict['players'] = saved_players_list
                            saved_data = json.dumps(saved_data_dict)
                            file.write(f"{stored_username}, {stored_password}, {saved_data}\n")
                        else:
                            file.write(user)
                # Reload updated saved data
                saved_data = reload_user_data(username)
    else:
        print(f"\nNo players found matching '{last_name}'.")
    input("\nPress Enter to return to the Logged In Menu...")
    main_menu()



def search_news():
    os.system('clear')
    search_input = input("Enter a keyword or phrase to search for in the news headlines: ").lower()
    news_folder = "News"
    matching_articles = []

    if not os.path.exists(news_folder):
        print("\nThe News folder does not exist.")
        input("\nPress Enter to return to the Main Menu...")
        main_menu()
        return

    for news_file in os.listdir(news_folder):
        if news_file.endswith(".txt"):
            with open(os.path.join(news_folder, news_file), 'r') as file:
                lines = file.readlines()
                if len(lines) > 0:
                    header = lines[0].strip().lower()
                    if search_input in header:
                        matching_articles.append((news_file, header))

    if matching_articles:
        print(f"\nNews articles matching '{search_input}':")
        for index, (news_file, header) in enumerate(matching_articles, start=1):
            print(f"{index}. {header}")

        read_choice = input("\nWould you like to read any of these articles? Enter the number or 'n' to skip: ")
        if read_choice.isdigit() and 1 <= int(read_choice) <= len(matching_articles):
            selected_article = matching_articles[int(read_choice) - 1][0]
            with open(os.path.join(news_folder, selected_article), 'r') as file:
                print("\n" + file.read())
    else:
        print(f"\nNo news articles found matching '{search_input}'.")

    input("\nPress Enter to return to the Main Menu...")
    main_menu()


if __name__ == "__main__":
    main_menu()