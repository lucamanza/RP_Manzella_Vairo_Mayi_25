# GitHub Repository Setup Instructions

## 🚀 Per chi riceve questa cartella

Se hai ricevuto questa cartella da qualcun altro, **prima** di seguire le istruzioni qui sotto, devi:

1. **Installare Python e pygame** (se non già installato)

RECATI SULLA CARTELLA con cd
APRI AMBIENTE VIRTUALE / INSTALLA I REQUISITI E TESTA IL GIOCO:
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 game.py


2. **Inizializzare il repository git locale** (vedi Step 2)
3. **Poi** seguire tutti gli altri step

## 🎮 Test rapido del gioco

Prima di tutto, testa che il gioco funzioni:

```bash
# Installa pygame se non è già installato
pip install pygame

# Testa il gioco
python game.py
```

Se il gioco si apre e funziona, procedi con la creazione del repository GitHub.

## Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in to your account
2. Click the "+" icon in the top right corner and select "New repository"
3. Set the repository name to: `RP_Manzella_Vairo_Mayi_25`
4. Make sure it's set to **Public** (so it can be shared)
5. **DO NOT** initialize with README, .gitignore, or license (we already have files)
6. Click "Create repository"

## Step 2: Connect Local Repository to GitHub

**IMPORTANTE**: Se hai ricevuto questa cartella da qualcun altro, devi prima eseguire questi comandi per inizializzare il repository git locale:

```bash
# Naviga nella cartella del progetto (sostituisci con il percorso della TUA cartella)
cd /percorso/della/tua/cartella

# Inizializza il repository git (solo se non esiste già)
git init

# Aggiungi tutti i file
git add .

# Fai il commit iniziale
git commit -m "Initial commit with game implementation"

# Crea i branch
git checkout -b Game
git checkout main
git checkout -b ROS
git add ros_placeholder.py
git commit -m "Add ROS placeholder file"
```

Poi, dopo aver creato la repository su GitHub, connetti il repository locale:

```bash
# Aggiungi il remote origin (sostituisci YOUR_USERNAME con il tuo username GitHub)
git remote add origin https://github.com/lucamanza/RP_Manzella_Vairo_Mayi_25.git

# Pusha il branch main
git checkout main
git push -u origin main

# Pusha il branch Game
git checkout Game
git push -u origin Game

# Pusha il branch ROS
git checkout ROS
git push -u origin ROS
```

## Step 3: Share Repository

1. Go to your repository settings on GitHub
2. Click on "Manage access" or "Collaborators"
3. Click "Add people" or "Invite a collaborator"
4. Enter the email: `sacarras@ing.uc3m.es`
5. Send the invitation

## Step 4: Verify Setup

- [ ] Repository name: `RP_Manzella_Vairo_Mayi_25`
- [ ] Two branches: `Game` and `ROS`
- [ ] `game.py` file in the `Game` branch
- [ ] Repository shared with `sacarras@ing.uc3m.es`
- [ ] Game features working correctly

## Game Features Implemented

✅ **Welcome Screen**: Press SPACE to start  
✅ **Player Control**: Arrow keys or WASD movement  
✅ **Obstacles/Enemies**: Red enemies that move automatically  
✅ **Collisions**: Lose lives when touching enemies  
✅ **Score System**: Collect yellow items for points  
✅ **Display Score**: Current score shown on screen  
✅ **End Game Screen**: Final score with restart/exit options  
✅ **Increasing Difficulty**: Speed and enemy spawn rate increase with levels  
✅ **Game Speed Control**: 60 FPS with smooth movement  
✅ **Purple Player**: Player represented by purple circle  
✅ **Screen Size**: 800x600 pixels  

## How to Run the Game

```bash
# Install dependencies
pip install -r requirements.txt

# Run the game
python game.py
```
