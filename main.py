from PIL import Image

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # Open and get image size
    img = Image.open(image)
    width, height = img.size

    # Resize image
    new_width = width // scale
    new_width -= new_width % 2
    new_height = height // scale
    new_height -= new_height % 2
    img.resize((new_width, new_height)).save("resized.%s" % type)

    # Open new image
    img = Image.open("resized.%s" % type)

    # List w/ correct dimensions
    grid = []
    for i in range(new_height):
        grid.append(["X"] * (new_width))
    
    pix = img.load()

    for y in range(new_height):
        for x in range(new_width):
            if sum(pix[x,y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pix[x,y]) in range(100,200):
                grid[y][x] = "%"
            elif sum(pix[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pix[x,y]) in range(300,400):
                grid[y][x] = "*"
            elif sum(pix[x,y]) in range(400,500):
                grid[y][x] = "+"
            elif sum(pix[x,y]) in range(500,600):
                grid[y][x] = "/"
            elif sum(pix[x,y]) in range(600,700):
                grid[y][x] = "("
            elif sum(pix[x,y]) in range(700,750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
        
    art = open(saveas, "w")

    for row in grid:
        art.write("".join(row) + "\n")
    
    art.close()

def main():
        path = input("Enter the path to the image: \n")
        print("Thank you!")
        name = path.split(".")[0]
        file_type = path.split(".")[1]
        asciiConvert(path, file_type, name + ".txt", "1")

if __name__ == "__main__":
    main()