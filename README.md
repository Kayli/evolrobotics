# Evolving Robotics Project

This repository contains lecture transcripts and processing tools for an Evolutionary Robotics course. The course covers a comprehensive range of topics in evolutionary robotics, from fundamental concepts to advanced applications.

## Course Content

The course includes lectures on:
- Artificial Intelligence History
- Embodied Cognition
- Artificial Neural Networks
- Evolutionary Algorithms
- Physical Simulation
- Continuous Time Recurrent Neural Networks (CTRNNs)
- Minimal Cognition
- Active Categorical Perception
- Bipedal Locomotion
- Modularity
- NEAT/HyperNEAT Algorithms
- Reality Gap in Robotics
- The GOLEM Project
- Resilient Machines
- Transferability in Robotics
- Twitch Plays Robotics
- Evolution of Teamwork and Communication
- Soft Robotics
- Biological Robots (Xenobots)

## Tools

### Transcript Processing

The repository includes a Python script (`main.py`) that processes VTT format lecture transcripts into plain text. The script:
- Removes timestamps and formatting tags
- Eliminates duplicate lines
- Organizes content by lecture
- Outputs clean, readable text

## Usage

To process the lecture transcripts:
```bash
python main.py
```
This will generate a cleaned transcript file named `cleaned_output_plain.txt`.
