const profileData = {
    name: "Vishal AA",
    age: 25,
    location: "Currently in Bangalore.",
    bio: "I am a multi-tasking individual with good gaming skills. But I ain't a pro in that.",
    interests: ["Gardening", "Cooking", "Hunting", "Painting"],
    socialLinks: {
        github: "https://github.com/yourusername",
        linkedin: "https://www.linkedin.com/in/yourprofile",
        twitter: "https://twitter.com/yourusername"
    },
    profileImage: "https://cdn.britannica.com/36/198336-050-A9B8AA86/Chadwick-Boseman-Tchalla-Black-Panther-Black.jpg"
};

document.getElementById("loadProfileBtn").addEventListener("click", function () {
    const profileContent = document.getElementById("profileContent");
    profileContent.innerHTML = `
        <p><strong>Name:</strong> ${profileData.name}</p>
        <p><strong>Age:</strong> ${profileData.age}</p>
        <p><strong>Location:</strong> ${profileData.location}</p>
        <p><strong>Bio:</strong> ${profileData.bio}</p>
        <p><strong>Interests:</strong> ${profileData.interests.join(", ")}</p>
        <p><strong>Social Links:</strong></p>
        <p><strong>Profile Image:</strong> ${profileData.profileImage}</p>
        <a href=" ${profileData.profileImage}" target="_blank">Profile Image</a>
        <ul>
            <li><a href="${profileData.socialLinks.github}" target="_blank">GitHub</a></li>
            <li><a href="${profileData.socialLinks.linkedin}" target="_blank">LinkedIn</a></li>
            <li><a href="${profileData.socialLinks.twitter}" target="_blank">Twitter</a></li>
        </ul>
    `;
});
