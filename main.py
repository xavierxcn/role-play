import player


def main():
    text = ""
    with open("诛仙.md", 'r') as f:
        lines = f.readlines()[-200:]
        for line in lines:
            l = line.strip()
            if l == "":
                continue
            text += l

    print(len(text))

    player1 = player.Player("张小凡", text)
    player2 = player.Player("碧瑶", text)

    player1.talk_to(player2)
    player2.talk_to(player1)

    start_word = "你可后悔为我挡下诛仙剑？"

    player1.messages.append({"role": "assistant", "content": start_word})
    print(f"{player1.name}: {start_word}")
    player2.listen("你可后悔为我挡下诛仙剑？")

    # 交替对话
    times = 0
    while times < 10:
        listener = player1 if times % 2 == 0 else player2
        talker = player2 if times % 2 == 0 else player1
        words = ""
        print(f"{talker.name}: ", end='')
        for chunk in talker.say():
            print(chunk, end='')
            words += chunk
        listener.listen(words)
        talker.messages.append({"role": "assistant", "content": words})
        times += 1
        print()
    player1.save()
    player2.save()




if __name__ == '__main__':
    main()