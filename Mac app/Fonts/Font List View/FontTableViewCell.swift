//
//  FontTableViewCell.swift
//  Fonts
//
//  Created by Miotke, Andrew on 1/4/21.
//

import UIKit

class FontTableViewCell: UITableViewCell {
    
    static let reuseId = "FontTableViewCell"
    
    // UI elements
    let fontPreviewLabel = UILabel()
    let enableFontToggle = UISwitch()
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: "FontTableViewCell")
        
        selectionStyle = .none
        layoutUI()
        defaultValues()
    }
    
    private func defaultValues() {
        // This method can go away once data from the API starts coming in.
        fontPreviewLabel.text = "Font Preview"
        enableFontToggle.isOn = false
        
        fontPreviewLabel.font = fontPreviewLabel.font.withSize(50)
        enableFontToggle.transform = CGAffineTransform(scaleX: 1.25, y: 1.25)
    }
    
    private func layoutUI() {
        let padding: CGFloat = 10

        addSubview(fontPreviewLabel)
        addSubview(enableFontToggle)
        fontPreviewLabel.translatesAutoresizingMaskIntoConstraints = false
        enableFontToggle.translatesAutoresizingMaskIntoConstraints = false
        
        NSLayoutConstraint.activate([
            fontPreviewLabel.centerYAnchor.constraint(equalTo: self.centerYAnchor),
            fontPreviewLabel.leadingAnchor.constraint(equalTo: self.leadingAnchor, constant: padding),

            enableFontToggle.trailingAnchor.constraint(equalTo: self.trailingAnchor, constant: -20),
            enableFontToggle.centerYAnchor.constraint(equalTo: self.centerYAnchor),
            
            self.heightAnchor.constraint(equalToConstant: 150)
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
