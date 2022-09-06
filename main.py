from game import Game

def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

    # dict = {
    #     'SNAKE' : {
    #         'HEAD' : 1,
    #         'BODY' : 2,
    #         'TAIL' : 3
    #     },
    #     'FOOD' : 2
    # }
    
    # dataString = json.dumps(dict, indent=4)
    # print(dataString)
    
    # print(dict)
    
    # with open('./data/info.json', 'w') as file:
    #     json.dump(dict, file, indent=4)
    # file.close()
    
    # with open('./data/info.json', 'r') as file:
    #     tempDict = json.load(file)
    #     file.close()
    # print(tempDict)
