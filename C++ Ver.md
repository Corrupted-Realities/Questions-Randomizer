#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>

void randomizeFileLines(const std::string& inputFileName) {
    std::ifstream inputFile(inputFileName);
    
    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open the file " << inputFileName << std::endl;
        return;
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(inputFile, line)) {
        lines.push_back(line);
    }

    inputFile.close();

    std::srand(static_cast<unsigned int>(std::time(0)));
    std::random_shuffle(lines.begin(), lines.end());
    std::string outputFileName = inputFileName.substr(0, inputFileName.find_last_of(".")) + "Rand.txt";
    std::ofstream outputFile(outputFileName);

    if (!outputFile.is_open()) {
        std::cerr << "Error: Could not create the output file " << outputFileName << std::endl;
        return;
    }
    int lineNumber = 1;
    for (const auto& randomizedLine : lines) {
        outputFile << lineNumber << ") " << randomizedLine << std::endl;
        lineNumber++;
    }

    outputFile.close();
    std::cout << "Randomized lines saved to " << outputFileName << std::endl;
}

int main() {
    std::string inputFileName;
    
    std::cout << "Enter the name of the text file: ";
    std::cin >> inputFileName;

    randomizeFileLines(inputFileName);

    return 0;
}

