# CounterfitFinalProject
[About](#About) | [Getting Started](#Getting-Started) | [Learn More](#Learn-More) |  [Acknowledgments](#Acknowledgments) | [Contributing](#Contributing) | [Trademarks](#Trademarks) | [Contact Us](#Contact-Us)

```
---------------------------------------------------
Microsoft
                          __            _____ __
  _________  __  ______  / /____  _____/ __(_) /_
 / ___/ __ \/ / / / __ \/ __/ _ \/ ___/ /_/ / __/
/ /__/ /_/ / /_/ / / / / /_/  __/ /  / __/ / /
\___/\____/\__,_/_/ /_/\__/\___/_/  /_/ /_/\__/

                                        #ATML

---------------------------------------------------
```

## About
Counterfit is a command-line tool and generic automation layer for assessing the security of machine learning systems.

## Getting Started
Choose one of these methods to get started quickly:
* [Option 1: Deploy via Azure Shell](#Option-1-Deploy-now-on-Azure-via-Azure-Shell)
* [Option 2: Setup an Anaconda Python environment and install locally](#Option-2-Setup-an-Anaconda-Python-environment-and-install-locally)

For more information including alternative installation instructions, please visit our [wiki](https://github.com/Azure/counterfit/wiki).

### Option 1: Deploy via Azure Shell
To run Counterfit from your browser
1. Click the button below to initiate small resource deployment to your Azure account.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure%2Fcounterfit%2Fmaster%2Finfrastructure%2Fazuredeploy.json) 

2. In the configuration blade, specify your subscription and resource group.
3. In your [Azure Shell](https://shell.azure.com), type the following, replacing `RESOURCE_GROUP` with the name of the resource group selected in the previous step.
```
az container exec --resource-group RESOURCE_GROUP --name counterfit --exec-command '/bin/bash'
```
4. Within the container, launch Counterfit.
```
python counterfit.py
```

### Option 2: Setup an Anaconda Python environment and install locally

1. Install [Anaconda Python](https://www.anaconda.com/products/individual) and [git](https://git-scm.com/downloads).
2. Clone this repository.
```
git clone https://github.com/Azure/counterfit.git
```
3. Open an Anaconda shell and create a virtual environment and dependencies.
```
cd counterfit
conda create --yes -n counterfit python=3.7
conda activate counterfit
pip install -r requirements.txt
```
4. Launch Counterfit.
```
python counterfit.py
```

## Testing AI tools for Security and Vulnerabilities 
### Demo 1 
There are two catdegory of images in the Satellite images environment which are stadiums and airplane strips. The AI system is built to determine what category each image belongs to. The goal of this attack is to try to make the AI system choose wrongly.
1. Interact with the target environment
```
interact satelliteimages
```
2. Load ART framework
```
load art
```
3. Use hop_skip_jump attack 
```
use hop_skip_jump
```
4. Set parameters for the attack.
```
set init_size=50 max_iter=20 max_eval=500
```
5. Use command predict to see initial scoring
```
predict
```
6. Run attack
```
run
```
7. Run the results
```
predict -r
```

### Demo 2
There are two catdegory of reviews in the moviereviews environment which are positives and negatives. The AI system is built to determine what category each review belongs to. The goal of this attack is to try to make the AI system choose wrongly.
1. Interact with the target environment
```
interact moviereviews
```
2. Load ART framework
```
load textattack
```
3. Use deepwordbug attack 
```
use deepwordbug
```
4. Use command predict to see initial scoring
```
predict
```
5. Run attack
```
run
```
6. Run the results
```
predict -r
```
## Learn More

Visit our [wiki](https://github.com/Azure/counterfit/wiki) for more detailed instructions on
* [Basic Use](https://github.com/Azure/counterfit/wiki/Basic-Use)
* [Tutorials](https://github.com/Azure/counterfit/wiki/Tutorials)
* [Counterfit Internals](https://github.com/Azure/counterfit/wiki/Internals)
* [Advanced Use](https://github.com/Azure/counterfit/wiki/Advanced-Use)
* [Assessment Guidance](https://github.com/Azure/counterfit/wiki/Assessment-Guidance)
* [Defensive Guidance](https://github.com/Azure/counterfit/wiki/Defensive-Guidance)

## Acknowledgments

Counterfit leverages excellent open source projects, including, [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) and [TextAttack](https://github.com/QData/TextAttack).

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## Contact Us

For comments or questions about how to leverage Counterfit, please contact <counterfithelpline@microsoft.com>. 
