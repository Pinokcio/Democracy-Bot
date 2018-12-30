import discord
import asyncio
import random

client = discord.Client()

up_size = 0
low_size = 0
upper = 0
lower = 0
col = 0
row = 0
arr = []
arr_int = []
flag = 0
def drawing(up, low):
    global col
    global row
    global arr
    global arr_int
    col = len(up*2)-1
    row = 8
    arr = [["　"]*col for i in range(row)]
    arr_int = [[0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if j%2 == 0:
                arr[i][j] = "l"
                arr_int[i][j] = 1
    for i in range(row):
        for j in range(col-2): 
            if arr_int[i][j] == 1:
                if random.randrange(1,4) == 1:
                    arr[i][j+1] = "ㅡ"
                    arr_int[i][j] = 2
                    arr_int[i][j+1] = 4
                    arr_int[i][j+2] = 3
            j = j+1
            
def riding(n):
    global arr_int
    i = 0
    j = n*2
    while(i!=8):
        if arr_int[i][j] == 2:
            j = j+2
            i = i+1
        elif arr_int[i][j] == 3:
            j = j-2
            i = i+1
        elif arr_int[i][j] == 1:
            i = i+1
    j = j/2
    return j

@client.event
async def on_message(message):
    global up_size
    global low_size
    global upper
    global lower
    global col
    global row
    global flag
    if message.content.startswith('!사다리설정'): #윗줄과 아랫줄의 값을 설정함
        arr_str = str(message.content).split(' ')
        if arr_str[1] == '0':
            upper = arr_str[2].split('/')
            if len(upper)>8:
                embed = discord.Embed(description = "사다리 윗줄이 너무 많아요!!\n(최대 8)")
                await client.send_message(message.channel,embed = embed)
                upper = []
            else:
                embed = discord.Embed(description = "윗줄 설정 완료.")
                await client.send_message(message.channel, embed = embed)
            up_size = len(upper)
        elif arr_str[1] == '1':
            lower = arr_str[2].split('/')
            if len(lower)>8:
                embed = discord.Embed(description = "사다리 아랫줄이 너무 많아요!!\n(최대 8)")
                await client.send_message(message.channel,embed = embed)
                lower = []
            else:
                embed = discord.Embed(description = "아랫줄 설정 완료.")
                await client.send_message(message.channel, embed = embed)
            low_size = len(lower)

    elif message.content.startswith('!설정완료'): #사다리 그리기
        if up_size!=low_size:
            embed = discord.Embed(description = "사다리 윗줄과 아랫줄의 크기가 다릅니다.")
            await client.send_message(message.channel, embed = embed)
        elif up_size == 0 | low_size == 0:
            embed = discord.Embed(description = "사다리 윗줄 혹은 아랫줄의 설정을 확인해주세요.")
            await client.send_message(message.channel, embed = embed)
        else:
            drawing(upper,lower)
            ms = ""
            for i in range(up_size):
                ms = ms + chr(49+i) + " : " + upper[i] + "　"*2 + chr(97+i) + " : " + lower[i] + "\n"
            for i in range(up_size):
                ms = ms + chr(49+i)
                if i!=up_size-1:
                    ms = ms + "..."
            ms = ms + "\n"
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    ms = ms + arr[i][j]
                ms = ms+"\n"
            for i in range(low_size):
                ms = ms + chr(97+i)
                if i!=up_size-1:
                    if i>=4:
                        ms = ms+"...."
                    else:
                        ms = ms + "..."
            embed = discord.Embed(title="사다리 탄다!!", description = ms)
            await client.send_message(message.channel,embed = embed)    
            up_result = []
            low_result = []
            for k in range(up_size):
                up_result.append(upper[k])
            for k in range(low_size):
                low_result.append(lower[k])
            flag = 1 
    elif message.content.startswith('!사다리진행'):
        arr_str = str(message.content).split(' ')
        if int(arr_str[1])>0 & int(arr_str[1])<up_size:
            pre_result = list(range(8))
            result = list(range(8))
            pre_result[int(arr_str[1])-1] = upper[int(arr_str[1])-1]
            result[int(arr_str[1])-1] = lower[int(riding(int(arr_str[1])-1))]
            embed = discord.Embed(description = pre_result[int(arr_str[1])-1] + " -> " + result[int(arr_str[1])-1])
            await client.send_message(message.channel,embed=embed)
        
    elif message.content.startswith('!사다리결과'):
        if flag==1:
            pre_result = list(range(8))
            result = list(range(8))
            ms_result = ""
            for i in range(up_size):
                pre_result[i] = upper[i]
                result[i] = lower[int(riding(i))]
                if i != up_size-1:
                    ms_result = ms_result + pre_result[i] + " -> " + result[i] + "\n"
                else:
                    ms_result = ms_result + pre_result[i] + " -> " + result[i]
            embed = discord.Embed(description = ms_result)
            await client.send_message(message.channel,embed=embed)
        else:
            embed = discord.Embed(description = "사다리 윗줄 혹은 아랫줄의 설정을 확인해주세요.")
            await client.send_message(message.channel, embed = embed)
            
    elif message.content.startswith('!설명'):
         embed = discord.Embed(description = "- 간단한 사다타기 기능을 가진 봇\n- 사다리를 텍스트 형식으로 출력\n- 명령어\n　- !사다리설정 (0 or 1) (ID1)/(ID2)/.../(IDn)\n　　- 0일 시 사다리타기 윗 줄 설정\n　　- 1일 시 사다리 타기 아랫 줄 설정\n　　- 윗 줄과 아랫 줄의 개수가 다를 경우 진행x\n　- !설정완료\n　　- 이 명령어를 입력할 때마다 새로운 사다리를 그림\n　- !사다리진행 (1~n)\n　　- 인덱스 값에 해당하는 ID의 사다리타기 결과 출력\n　- !사다리결과\n　　- 사다리타기의 모든 결과를 간단하게 출력")
         await client.send_message(message.channel, embed = embed)
        
client.run('NTI3NDY0OTc4ODgyNDk0NDY0.DwUIqw.lkxPaNA8oFlDtBR7hRr8vDVb5A4')
